'''
WebScraper to scrap and generate tracks.json file

Requirements:
beautifulsoup4==4.6.0
certifi==2017.7.27.1
chardet==3.0.4
html2text==2017.10.4
idna==2.6
requests==2.18.4
urllib3==1.22
'''

from bs4 import BeautifulSoup
import requests, json, re, html2text

h = html2text.HTML2Text()

print(" Parsing JSON File")

# Open tracks.json in read mode
tracks_file = open("tracks.json","r")
tracks = json.loads(tracks_file.read())
tracks = tracks['0.0.1'][0]
track_talks = []    # Holds the list of titles of all talks in tracks.json
for track in tracks:
    track_talks.append(str.lower(tracks[track]['title']))

print("\n     Total Talks in JSON File: "+str(len(track_talks)))

# Get all talks from https://in.pycon.org/cfp/2017/proposals
print(" Fetching Talks from Remote")
baseurl = "https://in.pycon.org"
r = requests.get(baseurl+"/cfp/2017/proposals/")
if(r.status_code!=200):
    print("Network Error: Status: "+r.status_code)
    exit()
soup = BeautifulSoup(r.text, "html.parser")
titles = soup.select(".proposal-list-content")
talks = {}          # Stores Matched Talks from Remote
counter = 0         # Stores Total Talks Scraped
total = len(titles) # Stores Total unmber of Talks from remote

print("\n     Total talks in remote: "+str(total))

def remove_white_space(text):
    '''
    Removes Whitespaces from Starting and End of Text
    '''
    return re.sub(r'(^\s{0,})|(\s{0,}$)',"",text)

# Start scraping the retreived talks from remote
for title in titles:
    counter = counter + 1
    
    url = baseurl+title.select(".proposal--title a")[0]["href"]
    right_section = title.select(".clearfix .pull-right b")
    
    # Remove " (~username)" from the speaker name and replace underscores by spaces
    speaker = re.sub(r'\s{0,}\(~[\w-]{0,}\)',"",remove_white_space(right_section[0].get_text())).replace("_"," ")
    # date = remove_white_space(right_section[1].get_text())
    
    print("\n\033[1m Scraping "+str(counter)+"/"+str(total)+" "+url+"\033[0m")
    
    rt = requests.get(url)
    
    page = BeautifulSoup(rt.text, "html.parser")

    proposal_title = remove_white_space(page.select(".proposal-title")[0].get_text())
    proposal_description = page.select(".proposal-writeup .proposal-writeup--section")
    proposal_type = str.lower(re.sub(r's$',"",page.select(".proposal-meta tr")[1].select("td")[1].get_text()))
    print("    Title: \033[4m"+proposal_title+"\033[0m by "+speaker+"\n     Type: "+proposal_type)

    if(str.lower(proposal_title) in track_talks):
        print("    \033[1;32;40m Match Found \033[0m")
        description = ""
        for section in proposal_description:
            # convert each section to markdown
            description += h.handle(str(section))
            #description += "<br>"
            #description += str(section.select(".heading")[0]) + "<br>"
            #for p in section.find_all("p"):
                #description+= str(p.replace("\n","<br>"))
        #description = description.replace("\n","<br>")
        description = description.replace("\n", "\\n")    # Escape Newline Characters
        talks.update({counter:{"title":proposal_title,"description":description,"type":proposal_type,"cfp":url,"speaker":{"name":speaker,"info":"","photo":""}}})
    else:
        print("    \033[1;31;40m Not Found \033[0m")

final_talks = {"0.0.1":[{}]}
for track in tracks:
    flag = 0
    track_title = tracks[track]["title"]
    for talk in talks:
        talk_title = talks[talk]["title"]
        if str.lower(track_title) == str.lower(talk_title):
            final_talks["0.0.1"][0].update({track:talks[talk]})
            flag = 1
    if flag == 0:
        try:
            print(tracks[track]["cfp"])
        except KeyError as e:
            tracks[track].update({"cfp":""})
        final_talks["0.0.1"][0].update({track:tracks[track]})
file_obj = open("tracks-new.json","w")
file_obj.write(json.dumps(final_talks))
