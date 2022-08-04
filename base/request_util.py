# _*_ coding:utf-8 _*_

import requests
"""
对 requests 发送请求封装成类：
1，支持 session 管理（可以定义 session 属性）
2，封装 visit 方法（可以发送 get 和 post 请求,delete请求，put请求）
"""
class HTTPHandle:

    def visit(self,url,method,params=None,data=None,**kwargs):
        if method.lower() == 'get':
            res=requests.get(url,params=params,**kwargs)
            try:
                return res.json()
            except ValueError:
                print("not json")
        elif method.lower()=='post':
            res=requests.post(url, data=data, **kwargs)
            try:
                return res.json()
            except ValueError:
                print("not json")
        elif method.lower()=='delete':
            res=requests.delete(url, **kwargs)
            try:
                return res.json()
            except ValueError:
                print("not json")
        else:
            res = requests.put(url, **kwargs)
            try:
                return res.json()
            except ValueError:
                print("not json")

# if __name__ == '__main__':
#     req = HTTPHandle().visit(method='get',
#                             url='http://web.juhe.cn/constellation/getAll',
#                             headers=None,
#                             params={
#                                 'consName':'天蝎座',
#                                 'type':'year',
#                                 'key':'8ffc14ff3cc065d7e76d122975f9517b'
#                             })
#     res = json.dumps(req,ensure_ascii=False)
#     print(res)
