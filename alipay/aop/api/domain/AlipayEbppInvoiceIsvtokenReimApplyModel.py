#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceIsvtokenReimApplyModel(object):

    def __init__(self):
        self._isv_app_code = None

    @property
    def isv_app_code(self):
        return self._isv_app_code

    @isv_app_code.setter
    def isv_app_code(self, value):
        self._isv_app_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_app_code:
            if hasattr(self.isv_app_code, 'to_alipay_dict'):
                params['isv_app_code'] = self.isv_app_code.to_alipay_dict()
            else:
                params['isv_app_code'] = self.isv_app_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceIsvtokenReimApplyModel()
        if 'isv_app_code' in d:
            o.isv_app_code = d['isv_app_code']
        return o


