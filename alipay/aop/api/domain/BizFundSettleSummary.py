#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizFundSettleSummary(object):

    def __init__(self):
        self._charge = None

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, value):
        self._charge = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge:
            if hasattr(self.charge, 'to_alipay_dict'):
                params['charge'] = self.charge.to_alipay_dict()
            else:
                params['charge'] = self.charge
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizFundSettleSummary()
        if 'charge' in d:
            o.charge = d['charge']
        return o


