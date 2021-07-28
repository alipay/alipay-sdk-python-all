#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayCodecHschoolDecodeUseModel(object):

    def __init__(self):
        self._code_value = None
        self._institution_code = None

    @property
    def code_value(self):
        return self._code_value

    @code_value.setter
    def code_value(self, value):
        self._code_value = value
    @property
    def institution_code(self):
        return self._institution_code

    @institution_code.setter
    def institution_code(self, value):
        self._institution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_value:
            if hasattr(self.code_value, 'to_alipay_dict'):
                params['code_value'] = self.code_value.to_alipay_dict()
            else:
                params['code_value'] = self.code_value
        if self.institution_code:
            if hasattr(self.institution_code, 'to_alipay_dict'):
                params['institution_code'] = self.institution_code.to_alipay_dict()
            else:
                params['institution_code'] = self.institution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayCodecHschoolDecodeUseModel()
        if 'code_value' in d:
            o.code_value = d['code_value']
        if 'institution_code' in d:
            o.institution_code = d['institution_code']
        return o


