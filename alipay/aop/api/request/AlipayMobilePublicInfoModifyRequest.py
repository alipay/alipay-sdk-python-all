#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayMobilePublicInfoModifyRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._app_name = None
        self._auth_pic = None
        self._license_url = None
        self._logo_url = None
        self._public_greeting = None
        self._shop_pic1 = None
        self._shop_pic2 = None
        self._shop_pic3 = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def auth_pic(self):
        return self._auth_pic

    @auth_pic.setter
    def auth_pic(self, value):
        self._auth_pic = value
    @property
    def license_url(self):
        return self._license_url

    @license_url.setter
    def license_url(self, value):
        self._license_url = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def public_greeting(self):
        return self._public_greeting

    @public_greeting.setter
    def public_greeting(self, value):
        self._public_greeting = value
    @property
    def shop_pic1(self):
        return self._shop_pic1

    @shop_pic1.setter
    def shop_pic1(self, value):
        self._shop_pic1 = value
    @property
    def shop_pic2(self):
        return self._shop_pic2

    @shop_pic2.setter
    def shop_pic2(self, value):
        self._shop_pic2 = value
    @property
    def shop_pic3(self):
        return self._shop_pic3

    @shop_pic3.setter
    def shop_pic3(self, value):
        self._shop_pic3 = value


    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.mobile.public.info.modify'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = json.dumps(obj=self.app_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_name'] = self.app_name
        if self.auth_pic:
            if hasattr(self.auth_pic, 'to_alipay_dict'):
                params['auth_pic'] = json.dumps(obj=self.auth_pic.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['auth_pic'] = self.auth_pic
        if self.license_url:
            if hasattr(self.license_url, 'to_alipay_dict'):
                params['license_url'] = json.dumps(obj=self.license_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['license_url'] = self.license_url
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = json.dumps(obj=self.logo_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['logo_url'] = self.logo_url
        if self.public_greeting:
            if hasattr(self.public_greeting, 'to_alipay_dict'):
                params['public_greeting'] = json.dumps(obj=self.public_greeting.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['public_greeting'] = self.public_greeting
        if self.shop_pic1:
            if hasattr(self.shop_pic1, 'to_alipay_dict'):
                params['shop_pic1'] = json.dumps(obj=self.shop_pic1.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_pic1'] = self.shop_pic1
        if self.shop_pic2:
            if hasattr(self.shop_pic2, 'to_alipay_dict'):
                params['shop_pic2'] = json.dumps(obj=self.shop_pic2.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_pic2'] = self.shop_pic2
        if self.shop_pic3:
            if hasattr(self.shop_pic3, 'to_alipay_dict'):
                params['shop_pic3'] = json.dumps(obj=self.shop_pic3.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_pic3'] = self.shop_pic3
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        return multipart_params
