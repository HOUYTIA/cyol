from PIL import Image,ImageDraw,ImageFont
import requests
import time
import sys
import os 
import re


class Get_QNDXX_Picture():
    def __init__(self,url):
        """
        获取最新大学习网址
        """
        response = requests.get(url)
        html = response.text.encode("ISO-8859-1").decode("utf-8") #爬取主网站信息
        pattern_url = r'<li><a href="(.*?)/m'
        all_url = re.findall(pattern_url,html) #得到很多青年大学习网址,最新的是第一个
        self.lastest_url = all_url[0]
        
    def get_body(self):
        """
        生成完成界面图片
        """
        image_body = requests.get(self.lastest_url+"/images/end.jpg") #从最新一期网页爬取完成图片
        with open("created\\body.jpg","wb") as file:
            file.write(image_body.content)
            file.close()

    def get_title(self):
        """
        生成头部
        """
        response_lastest_url = requests.get(self.lastest_url) #爬最新一期网页信息
        html_lastest = response_lastest_url.text.encode("ISO-8859-1").decode("utf-8")

        pattern_title = r'<title>(.*?)</title>'
        title = re.findall(pattern_title,html_lastest)[0] #获取最新一期标题
        #打开初始头部图片,将标题写入并保存
        image_title = Image.open("resources\\title.jpg")
        title_draw = ImageDraw.Draw(image_title)
        font = ImageFont.truetype("resources\\HarmonyOS_Sans_SC_Regular.ttf", 37, encoding="unic")
        title_draw.text((170, 5), title, 'black', font)
        image_title.save("created\\new_title.jpg","jpeg")

    def get_phone_title(self):
        # 获取当前系统时间保留成 小时:分钟 形式
        t = time.ctime()
        pattern = r" ([0-9]{2}:[0-9]{2})"
        now_time = re.findall(pattern,t)
        if now_time[0][0] == "0":
            now_time[0] = now_time[0].replace("0","")
        
        #打开初始手机状态栏图片,将时间写入并保存
        image_title = Image.open("resources/title1.jpg")
        title_draw = ImageDraw.Draw(image_title)
        font = ImageFont.truetype("resources\\HarmonyOS_Sans_SC_Regular.ttf", 30, encoding="unic")
        title_draw.text((10, 20), now_time[0], 'black', font)
        image_title.save("created\\new_phone_title.jpg","jpeg")
    
    def finished(self):
        img = Image.new('RGB', (828, 1489), (255, 255, 255))
        img.paste(Image.open("created\\new_phone_title.jpg"),(0, 0, 828, 70))
        img.paste(Image.open("created\\new_title.jpg"), (0, 70, 828, 145))
        img.paste(Image.open("created\\body.jpg"), (0, 145, 828, 1489))
        img.paste(Image.open("created\\body.jpg"), (0, 145, 828, 1489))
        img.save("new.jpg","jpeg")



if __name__ == "__main__":
    cwd = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(cwd)
    url = "http://news.cyol.com/gb/channels/vrGlAKDl/index.html" #大学习主网站
    qndxx = Get_QNDXX_Picture(url)
    qndxx.get_body()
    qndxx.get_title()
    qndxx.get_phone_title()
    qndxx.finished()
    input("运行完毕")

