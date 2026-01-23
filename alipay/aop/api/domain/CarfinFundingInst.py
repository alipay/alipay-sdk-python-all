#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinFundingInst(object):

    def __init__(self):
        self._funding_inst_name = None
        self._funding_inst_short_name = None
        self._funding_inst_uscc = None

    @property
    def funding_inst_name(self):
        return self._funding_inst_name

    @funding_inst_name.setter
    def funding_inst_name(self, value):
        self._funding_inst_name = value
    @property
    def funding_inst_short_name(self):
        return self._funding_inst_short_name

    @funding_inst_short_name.setter
    def funding_inst_short_name(self, value):
        self._funding_inst_short_name = value
    @property
    def funding_inst_uscc(self):
        return self._funding_inst_uscc

    @funding_inst_uscc.setter
    def funding_inst_uscc(self, value):
        self._funding_inst_uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.funding_inst_name:
            if hasattr(self.funding_inst_name, 'to_alipay_dict'):
                params['funding_inst_name'] = self.funding_inst_name.to_alipay_dict()
            else:
                params['funding_inst_name'] = self.funding_inst_name
        if self.funding_inst_short_name:
            if hasattr(self.funding_inst_short_name, 'to_alipay_dict'):
                params['funding_inst_short_name'] = self.funding_inst_short_name.to_alipay_dict()
            else:
                params['funding_inst_short_name'] = self.funding_inst_short_name
        if self.funding_inst_uscc:
            if hasattr(self.funding_inst_uscc, 'to_alipay_dict'):
                params['funding_inst_uscc'] = self.funding_inst_uscc.to_alipay_dict()
            else:
                params['funding_inst_uscc'] = self.funding_inst_uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinFundingInst()
        if 'funding_inst_name' in d:
            o.funding_inst_name = d['funding_inst_name']
        if 'funding_inst_short_name' in d:
            o.funding_inst_short_name = d['funding_inst_short_name']
        if 'funding_inst_uscc' in d:
            o.funding_inst_uscc = d['funding_inst_uscc']
        return o


