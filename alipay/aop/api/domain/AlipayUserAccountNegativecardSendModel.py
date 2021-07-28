#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountNegativecardSendModel(object):

    def __init__(self):
        self._arguments = None
        self._ext_info = None
        self._service_code = None
        self._user_id = None

    @property
    def arguments(self):
        return self._arguments

    @arguments.setter
    def arguments(self, value):
        self._arguments = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.arguments:
            if hasattr(self.arguments, 'to_alipay_dict'):
                params['arguments'] = self.arguments.to_alipay_dict()
            else:
                params['arguments'] = self.arguments
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
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
        o = AlipayUserAccountNegativecardSendModel()
        if 'arguments' in d:
            o.arguments = d['arguments']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


