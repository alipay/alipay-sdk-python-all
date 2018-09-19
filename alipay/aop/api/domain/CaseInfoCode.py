#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CaseInfoCode(object):

    def __init__(self):
        self._info_code = None
        self._info_code_desc = None

    @property
    def info_code(self):
        return self._info_code

    @info_code.setter
    def info_code(self, value):
        self._info_code = value
    @property
    def info_code_desc(self):
        return self._info_code_desc

    @info_code_desc.setter
    def info_code_desc(self, value):
        self._info_code_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.info_code:
            if hasattr(self.info_code, 'to_alipay_dict'):
                params['info_code'] = self.info_code.to_alipay_dict()
            else:
                params['info_code'] = self.info_code
        if self.info_code_desc:
            if hasattr(self.info_code_desc, 'to_alipay_dict'):
                params['info_code_desc'] = self.info_code_desc.to_alipay_dict()
            else:
                params['info_code_desc'] = self.info_code_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaseInfoCode()
        if 'info_code' in d:
            o.info_code = d['info_code']
        if 'info_code_desc' in d:
            o.info_code_desc = d['info_code_desc']
        return o


