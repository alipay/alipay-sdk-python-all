#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenAccessCodeDTO(object):

    def __init__(self):
        self._access_code = None
        self._expire_time = None

    @property
    def access_code(self):
        return self._access_code

    @access_code.setter
    def access_code(self, value):
        self._access_code = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_code:
            if hasattr(self.access_code, 'to_alipay_dict'):
                params['access_code'] = self.access_code.to_alipay_dict()
            else:
                params['access_code'] = self.access_code
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenAccessCodeDTO()
        if 'access_code' in d:
            o.access_code = d['access_code']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        return o


