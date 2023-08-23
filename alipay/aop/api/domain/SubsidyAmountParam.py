#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubsidyAmountParam(object):

    def __init__(self):
        self._subsidy_amount = None
        self._subsidy_mode = None
        self._subsidy_type = None

    @property
    def subsidy_amount(self):
        return self._subsidy_amount

    @subsidy_amount.setter
    def subsidy_amount(self, value):
        self._subsidy_amount = value
    @property
    def subsidy_mode(self):
        return self._subsidy_mode

    @subsidy_mode.setter
    def subsidy_mode(self, value):
        self._subsidy_mode = value
    @property
    def subsidy_type(self):
        return self._subsidy_type

    @subsidy_type.setter
    def subsidy_type(self, value):
        self._subsidy_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.subsidy_amount:
            if hasattr(self.subsidy_amount, 'to_alipay_dict'):
                params['subsidy_amount'] = self.subsidy_amount.to_alipay_dict()
            else:
                params['subsidy_amount'] = self.subsidy_amount
        if self.subsidy_mode:
            if hasattr(self.subsidy_mode, 'to_alipay_dict'):
                params['subsidy_mode'] = self.subsidy_mode.to_alipay_dict()
            else:
                params['subsidy_mode'] = self.subsidy_mode
        if self.subsidy_type:
            if hasattr(self.subsidy_type, 'to_alipay_dict'):
                params['subsidy_type'] = self.subsidy_type.to_alipay_dict()
            else:
                params['subsidy_type'] = self.subsidy_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubsidyAmountParam()
        if 'subsidy_amount' in d:
            o.subsidy_amount = d['subsidy_amount']
        if 'subsidy_mode' in d:
            o.subsidy_mode = d['subsidy_mode']
        if 'subsidy_type' in d:
            o.subsidy_type = d['subsidy_type']
        return o


