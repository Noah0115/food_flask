import os
from urllib.parse import quote,unquote

from app.config import STATIC_PREIFX

def url_parse(data):
    for i in data:
        results_url = STATIC_PREIFX+i["cover"].lstrip('.')
        results_encoded_url = quote(results_url, safe='/:')
        i["cover"] = results_encoded_url
    return data

def url_unparse(data):
    decoded_url = unquote(data)
    return decoded_url

def pic_parse(data):
    pic_result = []
    for i in data:
        pic_path = i["pic_path"]
        pic_path_split_ls = pic_path.split(",")
        for j in pic_path_split_ls:
            pic_url = STATIC_PREIFX + i["cover"].lstrip('.').replace('cover.jpg', j)
            pic_encoded_url = quote(pic_url, safe='/:')
            pic_result.append(pic_encoded_url)
        i["pic_path"] = pic_result
    return data

def step_parse(data):
    step_result = []
    for i in data:
        step = i["step"]
        step_split_ls = step.split("\n")
        for j in step_split_ls:
            step_result.append(j)
        i["step"] = step_result
    return data
