import json

ba = b'{"content": "\\u76ae\\u76ae\\u72ac\\u8fdb\\u5165'
bb = b'\\u623f\\u95f4\\n"}2xx@oo${"content": "\\u76ae\\u76ae\\u72ac\\u8fdb\\u5165'
bs = b'2xx@oo$n'

bl = ba + bb
data, tail = bl.split(bs)
print(data)
print(json.loads(data.decode("utf-8")))
print(tail)