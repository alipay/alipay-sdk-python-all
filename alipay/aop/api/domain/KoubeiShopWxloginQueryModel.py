#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiShopWxloginQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._grant_type = None
        self._js_code = None
        self._wx_app_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def grant_type(self):
        return self._grant_type

    @grant_type.setter
    def grant_type(self, value):
        self._grant_type = value
    @property
    def js_code(self):
        return self._js_code

    @js_code.setter
    def js_code(self, value):
        self._js_code = value
    @property
    def wx_app_id(self):
        return self._wx_app_id

    @wx_app_id.setter
    def wx_app_id(self, value):
        self._wx_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.grant_type:
            if hasattr(self.grant_type, 'to_alipay_dict'):
                params['grant_type'] = self.grant_type.to_alipay_dict()
            else:
                params['grant_type'] = self.grant_type
        if self.js_code:
            if hasattr(self.js_code, 'to_alipay_dict'):
                params['js_code'] = self.js_code.to_alipay_dict()
            else:
                params['js_code'] = self.js_code
        if self.wx_app_id:
            if hasattr(self.wx_app_id, 'to_alipay_dict'):
                params['wx_app_id'] = self.wx_app_id.to_alipay_dict()
            else:
                params['wx_app_id'] = self.wx_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiShopWxloginQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'grant_type' in d:
            o.grant_type = d['grant_type']
        if 'js_code' in d:
            o.js_code = d['js_code']
        if 'wx_app_id' in d:
            o.wx_app_id = d['wx_app_id']
        return o


