import requests,re,pandas,time
end_id='0';count=1;all_cnt=0;gacha=[];gacha_stars=[];gacha5=[];gacha5_count=[];cnt5=0;gacha4=[];gacha4_count=[];cnt4=0;start_time=time.time()
url='https://api-takumi.mihoyo.com/common/gacha_record/api/getGachaLog?authkey_ver=1&sign_type=2&auth_appid=webview_gacha&win_mode=fullscreen&gacha_id=1db86adac1dbe450484dfcdc4d2f8d1e634cfa&timestamp=1703634155&region=prod_gf_cn&default_gacha_type=11&lang=zh-cn&authkey=hPsnlGY9qBGqIs0n6Su5QBstyD0guy9opMh9r6JvE45IzZ%2BlbgftysJ1eDeE6A%2FmzD9Ayglctvr%2BEzcwyiggYCpKxoxgvbmeijiTiBV32ju%2Ffcy3pZ0xLuQLfXHjIIpz9G6X5PAob47loDybGyS9ehJ3pf43JR5P0%2BlwWLSHH4bIMdzipLjIfU97n3QxFZ1GavvFXwvhf0YfIbC8gn%2FgnsyEk1S4Cj3On2RFkYF8UMwxmjuQlrizJRUnemHbxoWq8%2FWTMsulskh11FrKvP8pdw2Uoqkd3APe46U7hDf4vwjlgS8KLa0z8dtZ7Yf7Vae5YFR79EMawQBKDS4k36KEvCycs36gM8vXKC1oIbNwQDtK%2ByRkhRCtA%2BEChPoZNRJD8yv7FP2fncn6RbmIzZb713hONYCWFpkRP9SPS9qjhJ9Idu3qo2x3nhUnFril1Tc25GnCUL4oqNtxmzYdIvHthithlfMbuLxq80h7i6AqnnqxAYhHHCNAqvZ7yRKtpPagrur7UoDbbXgl7JGSWa08onDn%2FqQdKcrupgr48c%2BnLv92ckWuzlVtYOe2CRZJivg9aeQ8n2VF%2BmmHkulRHgYlTjyQw1bhQ7uwR38HkjOccGEYjHc7ES%2BoRTAz0qndaKvUIsnLdN5QcNPInxhWcwlhCmxlmgvKERpwbesqD1wH%2BOE%3D&game_biz=hkrpg_cn&os_system=Windows%2011%20%20%2810.0.22631%29%2064bit&device_model=H610M%20S2%20DDR4%20%28Gigabyte%20Technology%20Co.%2C%20Ltd.%29&plat_type=pc&page=1&size=30&gacha_type=11&end_id='
while count!=0:
    resp=requests.get(url+end_id).text
    item=re.finditer(r'{"uid":".*?","gacha_id":".*?","gacha_type":".*?","item_id":".*?","count":".*?","time":".*?","name":"(?P<name>.*?)","lang":".*?","item_type":".*?","rank_type":"(?P<rank_type>.*?)","id":"(?P<id>.*?)"}',resp)
    count=0
    for j in item:
        gacha.append(j.group('name'));gacha_stars.append(j.group('rank_type'))
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