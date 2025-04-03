import { serve } from "https://deno.land/std@0.200.0/http/server.ts";

async function handler(req: Request): Promise<Response> {
  /*
  if (new URL(req.url).hostname.endsWith(".deno.dev")) {
    return new Response("404 Not Found", {status: 404,});
  }
  */
  const url = new URL(req.url)
  let filePath = url.pathname
  filePath = decodeURIComponent("." + filePath)
  try{
    const stat=await Deno.stat(filePath)
    if (stat.isDirectory){
      await Deno.stat(filePath+"/index.html")
      filePath=filePath+"/index.html"
    }
  }catch(_){
    try{
      await Deno.stat(filePath+".html")
      filePath=filePath+".html"
    }catch(_){
      //404
      try {
        const fileContent = await Deno.readFile('./404.html');
        return new Response(fileContent, {headers: {"Content-Type": 'text/html'}, status: 404})
      } catch (_) {
        return new Response("404 not found", {status: 404});
      }
    }
  }
  const range=req.headers.get("Range");
  const stat=await Deno.stat(filePath)
  const fileSize=stat.size
  let start = 0;
  let end: number | undefined = fileSize - 1;
  if (range){
    const matches = range.match(/bytes=(\d+)-(\d*)/);
    if (matches) {
      start = parseInt(matches[1], 10);
      end = matches[2] ? parseInt(matches[2], 10) : fileSize - 1;
      end = Math.min(end, fileSize - 1);
    }
  }
  const file = await Deno.open(filePath,{read:true})
  if (range){
    const buffer=new Uint8Array(end-start+1)
    const readableStream = file.readable
     .pipeThrough(new TransformStream({
       start() { file.seek(start, Deno.SeekMode.Start); },
       transform(chunk, controller) {
         // 仅返回指定范围内的数据
         controller.enqueue(chunk);
       },
     }));
    return new Response(readableStream, {status:206,headers: {"Content-Type": getContentType(filePath),"Content-Range":`bytes ${start}-${end}/${fileSize}`}});
  }
  return new Response(file.readable, {headers: {"Content-Type": getContentType(filePath)}});
}
function getContentType(fileName: string): string {
  const extension = fileName.split(".").pop();
  switch (extension) {
    case "html":
      return "text/html";
    case "css":
      return "text/css";
    case "js":
      return "application/javascript";
    case "json":
      return "application/json";
    case "png":
      return "image/png";
    case "jpg":
    case "jpeg":
      return "image/jpeg";
    case "gif":
      return "image/gif";
    case "txt":
      return "text/plain";
    default:
      return "application/octet-stream";
  }
}
// 启动服务器
serve(handler, { port: 8000 });