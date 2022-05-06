#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneMarketingEquitycodeDiscryptGetModel(object):

    def __init__(self):
        self._encrypted_code = None
        self._source = None

    @property
    def encrypted_code(self):
        return self._encrypted_code

    @encrypted_code.setter
    def encrypted_code(self, value):
        self._encrypted_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypted_code:
            if hasattr(self.encrypted_code, 'to_alipay_dict'):
                params['encrypted_code'] = self.encrypted_code.to_alipay_dict()
            else:
                params['encrypted_code'] = self.encrypted_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneMarketingEquitycodeDiscryptGetModel()
        if 'encrypted_code' in d:
            o.encrypted_code = d['encrypted_code']
        if 'source' in d:
            o.source = d['source']
        return o


