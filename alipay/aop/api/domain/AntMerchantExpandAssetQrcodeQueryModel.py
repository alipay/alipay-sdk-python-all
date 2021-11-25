#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandAssetQrcodeQueryModel(object):

    def __init__(self):
        self._code = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetQrcodeQueryModel()
        if 'code' in d:
            o.code = d['code']
        return o


