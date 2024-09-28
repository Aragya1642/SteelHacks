import requests

if __name__=='__main__':
    print("Hello World")
    url = r"http://breadboard-community.wl.r.appspot.com/boards/@AdorableFox/quest.bgl.api/run"
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
    print(url)
    print(requests.post(url,params=params))

