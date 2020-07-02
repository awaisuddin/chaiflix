
import os      
from bs4 import BeautifulSoup, SoupStrainer
import requests

i=1

while True:
    url = "https://vidcloud9.com/movies?page=" + str(i)
    #print("                                                           counter",str(i))

    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')
    x1 = " "
    counter = 0

    for link in soup.find_all('a'):
        if "videos" in str(link.get('href')):
            #print("\n")
            videowebsitelink="https://vidcloud9.com"+str(link.get('href'))
            #print(str(link.get('href')).replace("/videos/","").replace("-","+"))
            
            x = "https://www.google.com/search?sxsrf=ALeKk02TepDzilhakTKiwze2e510Z-l8Mg%3A1593521030145&ei=hjP7Xpa9CMmP4-EPz5K0oAo&q="+str(link.get('href')).replace("/videos/","").replace("-","+")+"+movie+ratings"

            #print(x)

            url1 = x            

            page1 = requests.get(url1)    
            data1 = page1.text
            soup1 = BeautifulSoup(data1, 'html.parser')
            imdb = ""
            rt = ""
            for link1 in soup1.find_all('span'):
                
                if "/10" in str(link1.get_text()):
                    imdb = ""
                    #print(link1.get_text(),"  imdb")
                    imdb = link1.get_text()
                    break
            for link2 in soup1.find_all('span'):
                
                if "%" in str(link2.get_text()):
                    rt = ""
                    #print(link2.get_text(),"  rotten tomatoes")
                    rt = link2.get_text()
                    break
                
            urls = videowebsitelink

            pages = requests.get(urls)    
            datas = pages.text
            soups = BeautifulSoup(datas, 'html.parser')

            for links in soups.find_all('iframe'):
                watchlink = "https:"+str(links.get('src'))
                counter = counter + 1
                #print("Watch Link: ",watchlink.replace(' ',''))

                for nm in soups.find_all('h1'):
                    name = ""
                    #print("Name: ",str(nm.get_text()).lower())
                    name = str(nm.get_text()).upper().replace("!","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").replace(":","").replace("'","").replace(",","").replace(".","").replace("/","").replace("}","").replace("{","")                                                                                          

                for img in soups.find_all('img'):
                    if "cover" in str(img.get('src')):
                        image = ""
                        #print("Cover Link: ",str(img.get('src')))
                        image = str(img.get('src'))
                        break
                    
                for des in soups.find_all('div'):
                    if "content-more-js" in str(des.get('class')):
                        description = str(des.get_text()).replace("\n						","")
                        #print(description)
                        break
            print("<a href = '/movies/allmovies/"+name+".html' class='gui-card'>")
            print("<div class='gui-card__media'>")
            print("<img class='gui-card__img' src='"+image+"' alt=''  />","  </div>")
            print("<div class='gui-card__details'>")
            print("<div class='gui-card__title'>")
            print(name)
            print("<br>IMDB Ratings: ",imdb)
            print("<br> Rottentomatoes: ",rt)
            print("</div> </div> </a>")

            # make the htmll player file
            

            #Link Html File Creator
            myFile = open(str(name)+'.html', 'w')
            myFile.write("<!DOCTYPE html>"
                        +"<html lang='en'>"
                        +"<head>"
                        +"<title>"
                        +"ChaiFlix"
                        +"</title>"
                        +"<meta charset='utf-8'>"
                        +"<meta http-equiv='X-UA-Compatible' content='IE=edge'>"
                        +"<meta name='description' content='Demo project'>"
                        +"<meta name='viewport' content='width=device-width, initial-scale=1'>"
                        +"<link rel='stylesheet' type='text/css' href='styles/bootstrap4/bootstrap.min.css'>"
                        +"<link href='plugins/font-awesome-4.7.0/css/font-awesome.min.css' rel='stylesheet' type='text/css'>"
                        +"<link rel='stylesheet' type='text/css' href='plugins/OwlCarousel2-2.2.1/owl.carousel.css'>"
                        +"<link rel='stylesheet' type='text/css' href='plugins/OwlCarousel2-2.2.1/owl.theme.default.css'>"
                        +"<link rel='stylesheet' type='text/css' href='plugins/OwlCarousel2-2.2.1/animate.css'>"
                        +"<link rel='stylesheet' type='text/css' href='plugins/jquery.mb.YTPlayer-3.1.12/jquery.mb.YTPlayer.css'>"
                        +"<link rel='stylesheet' type='text/css' href='styles/main_styles.css'>"
                        +"<link rel='stylesheet' type='text/css' href='styles/responsive.css'>"
                        +"<link rel='stylesheet' href='css/bootstrap.min.css'>"
                        +"<link rel='stylesheet' href='css/style.css'>"
                        +"<script src='js/index.js'>"
                        +"</script>"
                        +"</head>"
                        +"<body style='background-image: url('"
                        +image
                        +"');' >"
                        +"<div class='super_container'>"
                        +"<div class='home'>"	
                        +"<img style='position:relative;z-index:9999;height: 50px;' src='images/chaiflix.png'> <a> CHAIFLIX ===>   Instructions :  Single Click to (PAUSE) and (PLAY)          DOUBLE Click to (FullScreen)  </a>"
                        +"<div  class='home_slider_container'>"		
                        +"<iframe style='height: 100%; width: 100%;position: relative;'  allowfullscreen='true' frameborder='0' marginwidth='0' marginheight='0' scrolling='no' src='"
                        +watchlink
                        +"'>" 
                        +"</iframe>"	
                        +"</div>"
                        +"</div>"
                        +"<div class='home'>"
                        +"<div  class='home_slider_container'>"
                        +"<iframe style='height: 100%; width: 100%;position: relative;'  allowfullscreen='true' frameborder='0' marginwidth='0' marginheight='0' scrolling='no' src='playerslider.html'>" +"</iframe>"
                        +"</div>"
                        +"</div>"	
                        +"</div>"
                        +"</body>"
                        +"</html>")
            myFile.close()
            if counter%20==0:
                print('======================================================================Count( ',counter,' )========================================================================================' )
                
            
    i=i+1
    
'''<div class="gui-card">
            <div href = "" class="gui-card__media">
              <img class="gui-card__img" src="https://cdn.themovieseries.net/cover/inmate-1-the-rise-of-danny-trejo.png" alt=""  />
            </div>
            <div class="gui-card__details">
              <div class="gui-card__title">
                inmate #1: the rise of danny trejo
				<br> 100%  (5)    rotten tomatoes
              </div>
            </div>
          </div>'''

    
