#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RetailKbcodeCreateVo(object):

    def __init__(self):
        self._code_tip = None
        self._salesman = None

    @property
    def code_tip(self):
        return self._code_tip

    @code_tip.setter
    def code_tip(self, value):
        self._code_tip = value
    @property
    def salesman(self):
        return self._salesman

    @salesman.setter
    def salesman(self, value):
        self._salesman = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_tip:
            if hasattr(self.code_tip, 'to_alipay_dict'):
                params['code_tip'] = self.code_tip.to_alipay_dict()
            else:
                params['code_tip'] = self.code_tip
        if self.salesman:
            if hasattr(self.salesman, 'to_alipay_dict'):
                params['salesman'] = self.salesman.to_alipay_dict()
            else:
                params['salesman'] = self.salesman
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RetailKbcodeCreateVo()
        if 'code_tip' in d:
            o.code_tip = d['code_tip']
        if 'salesman' in d:
            o.salesman = d['salesman']
        return o


