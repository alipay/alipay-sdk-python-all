#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''


class AlipayClientConfig(object):

    def __init__(self, sandbox_debug=False):

        # 开发者应用id
        self._app_id = ''
        # 请求签名类型，推荐RSA2
        self._sign_type = 'RSA2'
        # 开发者应用私钥
        self._app_private_key = ''
        # 蚂蚁金服开放平台公钥
        self._alipay_public_key = ''

        # 蚂蚁金服开放平台网关地址
        self._server_url = "https://openapi.alipay.com/gateway.do"
        if sandbox_debug:
            self._server_url = "https://openapi.alipaydev.com/gateway.do"
        # 请求字符集，默认utf-8
        self._charset = 'utf-8'
        # 请求响应报文格式
        self._format = 'json'

        ## 以下为可选参数
        # 请求加密类型（对称加密算法）
        self._encrypt_type = ''
        # 请求加密密钥
        self._encrypt_key = ''
        # 请求读取超时，单位秒，默认15s
        self._timeout = 15

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value

    @property
    def sign_type(self):
        return self._sign_type

    @sign_type.setter
    def sign_type(self, value):
        self._sign_type = value

    @property
    def app_private_key(self):
        return self._app_private_key

    @app_private_key.setter
    def app_private_key(self, value):
        self._app_private_key = value

    @property
    def alipay_public_key(self):
        return self._alipay_public_key

    @alipay_public_key.setter
    def alipay_public_key(self, value):
        self._alipay_public_key = value

    @property
    def server_url(self):
        return self._server_url

    @server_url.setter
    def server_url(self, value):
        self._server_url = value

    @property
    def charset(self):
        return self._charset

    @charset.setter
    def charset(self, value):
        self._charset = value

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value

    @property
    def encrypt_key(self):
        return self._encrypt_key

    @encrypt_key.setter
    def encrypt_key(self, value):
        self._encrypt_key = value

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value



