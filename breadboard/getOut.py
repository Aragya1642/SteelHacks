import requests
import json

if __name__=='__main__':
    url = r"https://eden_byte-bbrunapiexample.web.val.run/"
    data = json.dumps('["input",{"node":{"type":"input","id":"input","configuration":{"schema":{"properties":{"context":{"type":"array","title":"Context","examples":[],"items":{"type":"object","behavior":["llm-content"]},"default":"[{\"role\":\"user\",\"parts\":[{\"text\":\"\"}]}]","description":"What events are you looking for?"}},"type":"object","required":[]}},"metadata":{"visual":{"x":-250,"y":311,"collapsed":"expanded"},"logLevel":"debug"}},"inputArguments":{"schema":{"properties":{"context":{"type":"array","title":"Context","examples":[],"items":{"type":"object","behavior":["llm-content"]},"default":"[{\"role\":\"user\",\"parts\":[{\"text\":\"\"}]}]","description":"What events are you looking for?"}},"type":"object","required":[]}},"path":[2],"bubbled":false,"timestamp":13203606.728505},"IwQINd44pIQ4DDNlAHf7"]')
    #params = {
    #          "$key": "bb-1t5q3bb3g5w6to47lv3j5k1y5c515g265i6b3o3k292g4t303h",
    #          "context": [
    #            {
    #              "role": "user",
    #              "parts": [
    #                {

    #                  "text": "How big is the moon?"
    #                }
    #              ]
    #            }
    #          ]
    #        }
    params = {
              "$key": "bb-1d34543t634r5lln245o6g1n1h1w5j635t5ega1n1o64115x49"
              }
    print(url)
    print(requests.post(url, data=data, verify=False))

