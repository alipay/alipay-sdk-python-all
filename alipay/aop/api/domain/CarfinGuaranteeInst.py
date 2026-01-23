#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinGuaranteeInst(object):

    def __init__(self):
        self._guarantee_inst_name = None
        self._guarantee_inst_short_name = None
        self._guarantee_inst_uscc = None

    @property
    def guarantee_inst_name(self):
        return self._guarantee_inst_name

    @guarantee_inst_name.setter
    def guarantee_inst_name(self, value):
        self._guarantee_inst_name = value
    @property
    def guarantee_inst_short_name(self):
        return self._guarantee_inst_short_name

    @guarantee_inst_short_name.setter
    def guarantee_inst_short_name(self, value):
        self._guarantee_inst_short_name = value
    @property
    def guarantee_inst_uscc(self):
        return self._guarantee_inst_uscc

    @guarantee_inst_uscc.setter
    def guarantee_inst_uscc(self, value):
        self._guarantee_inst_uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.guarantee_inst_name:
            if hasattr(self.guarantee_inst_name, 'to_alipay_dict'):
                params['guarantee_inst_name'] = self.guarantee_inst_name.to_alipay_dict()
            else:
                params['guarantee_inst_name'] = self.guarantee_inst_name
        if self.guarantee_inst_short_name:
            if hasattr(self.guarantee_inst_short_name, 'to_alipay_dict'):
                params['guarantee_inst_short_name'] = self.guarantee_inst_short_name.to_alipay_dict()
            else:
                params['guarantee_inst_short_name'] = self.guarantee_inst_short_name
        if self.guarantee_inst_uscc:
            if hasattr(self.guarantee_inst_uscc, 'to_alipay_dict'):
                params['guarantee_inst_uscc'] = self.guarantee_inst_uscc.to_alipay_dict()
            else:
                params['guarantee_inst_uscc'] = self.guarantee_inst_uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinGuaranteeInst()
        if 'guarantee_inst_name' in d:
            o.guarantee_inst_name = d['guarantee_inst_name']
        if 'guarantee_inst_short_name' in d:
            o.guarantee_inst_short_name = d['guarantee_inst_short_name']
        if 'guarantee_inst_uscc' in d:
            o.guarantee_inst_uscc = d['guarantee_inst_uscc']
        return o


