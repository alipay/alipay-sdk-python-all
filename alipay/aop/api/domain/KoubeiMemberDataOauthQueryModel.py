#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMemberDataOauthQueryModel(object):

    def __init__(self):
        self._auth_type = None
        self._code = None
        self._ext_info = None

    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMemberDataOauthQueryModel()
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'code' in d:
            o.code = d['code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        return o


