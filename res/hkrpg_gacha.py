import requests,re,pandas,time
end_id='0';count=1;all_cnt=0;gacha=[];gacha_stars=[];gacha5=[];gacha5_count=[];cnt5=0;gacha4=[];gacha4_count=[];cnt4=0;start_time=time.time()
url=input('粘贴链接，结尾为：size=20&gacha_type=任意&end_id=（size改为20，end_id后面没有数字）')
while count!=0:
    resp=requests.get(url+end_id).text
    item=re.finditer(r'{"uid":".*?","gacha_id":".*?","gacha_type":".*?","item_id":".*?","count":".*?","time":"(?P<time>.*?)","name":"(?P<name>.*?)","lang":".*?","item_type":".*?","rank_type":"(?P<rank_type>.*?)","id":"(?P<id>.*?)"}',resp)
    count=0
    for j in item:
        gacha.append(j.group('name')+j.group('time'));gacha_stars.append(j.group('rank_type'))
        count+=1
        end_id=j.group('id')
    all_cnt+=count;print(f'已分析：{all_cnt}抽')
print(f'共计：{len(gacha)}抽')
for i in range(len(gacha)):
    cnt5+=1;cnt4+=1
    if gacha_stars[-i]=='4':
        gacha4_count=[cnt4]+gacha4_count;gacha4=[gacha[-i]]+gacha4
        cnt4=0
    elif gacha_stars[-i]=='5':
        gacha5_count=[cnt5]+gacha5_count;gacha5=[gacha[-i]]+gacha5
        cnt5=0
df=pandas.DataFrame(['','']+gacha5_count+['','']+gacha4_count+['','']+gacha_stars+['',''],['','5星：']+gacha5+['','4星：']+gacha4+['','所有记录：']+gacha+['',f'共计：{len(gacha)}抽'],columns=['抽数/星级'])
df.to_excel('gacha.xlsx')
print(f'分析用时：{time.time()-start_time}s')