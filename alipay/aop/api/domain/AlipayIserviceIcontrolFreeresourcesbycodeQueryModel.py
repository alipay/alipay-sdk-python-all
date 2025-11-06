#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIcontrolFreeresourcesbycodeQueryModel(object):

    def __init__(self):
        self._biz_package_code = None

    @property
    def biz_package_code(self):
        return self._biz_package_code

    @biz_package_code.setter
    def biz_package_code(self, value):
        self._biz_package_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_package_code:
            if hasattr(self.biz_package_code, 'to_alipay_dict'):
                params['biz_package_code'] = self.biz_package_code.to_alipay_dict()
            else:
                params['biz_package_code'] = self.biz_package_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIcontrolFreeresourcesbycodeQueryModel()
        if 'biz_package_code' in d:
            o.biz_package_code = d['biz_package_code']
        return o


