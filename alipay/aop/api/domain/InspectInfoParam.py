#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InspectInfoParam(object):

    def __init__(self):
        self._consumables_price = None
        self._drug_price = None

    @property
    def consumables_price(self):
        return self._consumables_price

    @consumables_price.setter
    def consumables_price(self, value):
        self._consumables_price = value
    @property
    def drug_price(self):
        return self._drug_price

    @drug_price.setter
    def drug_price(self, value):
        self._drug_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.consumables_price:
            if hasattr(self.consumables_price, 'to_alipay_dict'):
                params['consumables_price'] = self.consumables_price.to_alipay_dict()
            else:
                params['consumables_price'] = self.consumables_price
        if self.drug_price:
            if hasattr(self.drug_price, 'to_alipay_dict'):
                params['drug_price'] = self.drug_price.to_alipay_dict()
            else:
                params['drug_price'] = self.drug_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InspectInfoParam()
        if 'consumables_price' in d:
            o.consumables_price = d['consumables_price']
        if 'drug_price' in d:
            o.drug_price = d['drug_price']
        return o


