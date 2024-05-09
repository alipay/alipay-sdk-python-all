#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubRentRiskItem(object):

    def __init__(self):
        self._risk_desc = None
        self._risk_name = None
        self._risk_rank = None

    @property
    def risk_desc(self):
        return self._risk_desc

    @risk_desc.setter
    def risk_desc(self, value):
        self._risk_desc = value
    @property
    def risk_name(self):
        return self._risk_name

    @risk_name.setter
    def risk_name(self, value):
        self._risk_name = value
    @property
    def risk_rank(self):
        return self._risk_rank

    @risk_rank.setter
    def risk_rank(self, value):
        self._risk_rank = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_desc:
            if hasattr(self.risk_desc, 'to_alipay_dict'):
                params['risk_desc'] = self.risk_desc.to_alipay_dict()
            else:
                params['risk_desc'] = self.risk_desc
        if self.risk_name:
            if hasattr(self.risk_name, 'to_alipay_dict'):
                params['risk_name'] = self.risk_name.to_alipay_dict()
            else:
                params['risk_name'] = self.risk_name
        if self.risk_rank:
            if hasattr(self.risk_rank, 'to_alipay_dict'):
                params['risk_rank'] = self.risk_rank.to_alipay_dict()
            else:
                params['risk_rank'] = self.risk_rank
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubRentRiskItem()
        if 'risk_desc' in d:
            o.risk_desc = d['risk_desc']
        if 'risk_name' in d:
            o.risk_name = d['risk_name']
        if 'risk_rank' in d:
            o.risk_rank = d['risk_rank']
        return o


