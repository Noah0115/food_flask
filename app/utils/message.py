import os

def success_msg(msg):
    """

    :param msg: 如果传入的是字符串，则正常返回json;如果是字典类型，则返回字典数据+消息模板
    :return:
    """
    if isinstance(msg, dict):
        resp = {
            "msg": "数据返回成功",
            "code": 200,
        }
        resp.update(msg)
        return resp
    elif isinstance(msg, list):
        resp = {"msg": "数据返回成功", "code": 200, 'data': msg}
        return resp
    elif isinstance(msg,tuple):
        resp = {"msg": "数据返回成功", "code": 200, 'data': list(msg)}
        return resp
    else:
        resp = {
            "msg": msg,
            "code": 200
        }
        return resp

def error_msg(msg):
    resp = {
        "msg": msg,
        "code": 500
    }
    return resp
