#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TbapiQueryAmountResponse(object):

    def __init__(self):
        self._amt_map = None
        self._available_group_amt = None

    @property
    def amt_map(self):
        return self._amt_map

    @amt_map.setter
    def amt_map(self, value):
        self._amt_map = value
    @property
    def available_group_amt(self):
        return self._available_group_amt

    @available_group_amt.setter
    def available_group_amt(self, value):
        self._available_group_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt_map:
            if hasattr(self.amt_map, 'to_alipay_dict'):
                params['amt_map'] = self.amt_map.to_alipay_dict()
            else:
                params['amt_map'] = self.amt_map
        if self.available_group_amt:
            if hasattr(self.available_group_amt, 'to_alipay_dict'):
                params['available_group_amt'] = self.available_group_amt.to_alipay_dict()
            else:
                params['available_group_amt'] = self.available_group_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TbapiQueryAmountResponse()
        if 'amt_map' in d:
            o.amt_map = d['amt_map']
        if 'available_group_amt' in d:
            o.available_group_amt = d['available_group_amt']
        return o


