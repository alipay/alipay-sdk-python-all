#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandActivitySignupQueryModel(object):

    def __init__(self):
        self._activity_code = None
        self._ext_info = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
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
        o = AntMerchantExpandActivitySignupQueryModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        return o


