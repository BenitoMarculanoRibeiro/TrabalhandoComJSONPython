from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
data = readfromstring(
    '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
)
print(json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml())