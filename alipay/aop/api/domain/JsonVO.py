#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JsonVO(object):

    def __init__(self):
        self._err_msg = None
        self._is_success = None

    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value


    def to_alipay_dict(self):
        params = dict()
        if self.err_msg:
            if hasattr(self.err_msg, 'to_alipay_dict'):
                params['err_msg'] = self.err_msg.to_alipay_dict()
            else:
                params['err_msg'] = self.err_msg
        if self.is_success:
            if hasattr(self.is_success, 'to_alipay_dict'):
                params['is_success'] = self.is_success.to_alipay_dict()
            else:
                params['is_success'] = self.is_success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JsonVO()
        if 'err_msg' in d:
            o.err_msg = d['err_msg']
        if 'is_success' in d:
            o.is_success = d['is_success']
        return o


