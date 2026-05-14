#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryEducertifyResultGetModel(object):

    def __init__(self):
        self._biz_id = None
        self._certify_auth_code = None
        self._certify_token = None
        self._open_id = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def certify_auth_code(self):
        return self._certify_auth_code

    @certify_auth_code.setter
    def certify_auth_code(self, value):
        self._certify_auth_code = value
    @property
    def certify_token(self):
        return self._certify_token

    @certify_token.setter
    def certify_token(self, value):
        self._certify_token = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.certify_auth_code:
            if hasattr(self.certify_auth_code, 'to_alipay_dict'):
                params['certify_auth_code'] = self.certify_auth_code.to_alipay_dict()
            else:
                params['certify_auth_code'] = self.certify_auth_code
        if self.certify_token:
            if hasattr(self.certify_token, 'to_alipay_dict'):
                params['certify_token'] = self.certify_token.to_alipay_dict()
            else:
                params['certify_token'] = self.certify_token
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayEbppIndustryEducertifyResultGetModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'certify_auth_code' in d:
            o.certify_auth_code = d['certify_auth_code']
        if 'certify_token' in d:
            o.certify_token = d['certify_token']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


