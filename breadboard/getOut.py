import requests

if __name__=='__main__':
    url = r"https://breadboard-community.wl.r.appspot.com/boards/@AdorableFox/quest.bgl.api/run"
    headers = {
      "Content-Type": "application/json",
    }
    params = {
              "$key": "bb-1t5q3bb3g5w6to47lv3j5k1y5c515g265i6b3o3k292g4t303h",
              "context": [
                {
                  "role": "user",
                  "parts": [
                    {
                      "text": "How big is the moon?"
                    }
                  ]
                }
              ]
            }
    #params = {
    #        
    #          "$key": "bb-1d34543t634r5lln245o6g1n1h1w5j635t5ega1n1o64115x49"
    #          }
    print(url)
    print(requests.post(url).status_code)#,params=params))

