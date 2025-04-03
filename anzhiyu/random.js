var posts=["2024/07/30/欢迎/","2025/01/29/test/","2024/07/30/Python下载/","2024/07/30/网址导航/","2024/07/30/hello-world/"];function toRandomPost(){
    window.location.href='/'+posts[Math.floor(Math.random() * posts.length)];
  };