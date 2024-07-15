#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateMultideductQueryModel(object):

    def __init__(self):
        self._biz_code = None
        self._open_id = None
        self._school_code = None
        self._token_id = None
        self._user_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def school_code(self):
        return self._school_code

    @school_code.setter
    def school_code(self, value):
        self._school_code = value
    @property
    def token_id(self):
        return self._token_id

    @token_id.setter
    def token_id(self, value):
        self._token_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.school_code:
            if hasattr(self.school_code, 'to_alipay_dict'):
                params['school_code'] = self.school_code.to_alipay_dict()
            else:
                params['school_code'] = self.school_code
        if self.token_id:
            if hasattr(self.token_id, 'to_alipay_dict'):
                params['token_id'] = self.token_id.to_alipay_dict()
            else:
                params['token_id'] = self.token_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateMultideductQueryModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'school_code' in d:
            o.school_code = d['school_code']
        if 'token_id' in d:
            o.token_id = d['token_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


