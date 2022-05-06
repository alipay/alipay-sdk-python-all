#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthKeywordIdentifyModel(object):

    def __init__(self):
        self._inst_name = None
        self._uscc = None

    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthKeywordIdentifyModel()
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


