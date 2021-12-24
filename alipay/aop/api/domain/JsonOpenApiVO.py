#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JsonOpenApiVO(object):

    def __init__(self):
        self._err_msg = None
        self._success = None

    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.err_msg:
            if hasattr(self.err_msg, 'to_alipay_dict'):
                params['err_msg'] = self.err_msg.to_alipay_dict()
            else:
                params['err_msg'] = self.err_msg
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JsonOpenApiVO()
        if 'err_msg' in d:
            o.err_msg = d['err_msg']
        if 'success' in d:
            o.success = d['success']
        return o


