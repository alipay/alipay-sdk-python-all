#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceFarmerproductionDeleteModel(object):

    def __init__(self):
        self._farmer_item_id = None

    @property
    def farmer_item_id(self):
        return self._farmer_item_id

    @farmer_item_id.setter
    def farmer_item_id(self, value):
        self._farmer_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.farmer_item_id:
            if hasattr(self.farmer_item_id, 'to_alipay_dict'):
                params['farmer_item_id'] = self.farmer_item_id.to_alipay_dict()
            else:
                params['farmer_item_id'] = self.farmer_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceFarmerproductionDeleteModel()
        if 'farmer_item_id' in d:
            o.farmer_item_id = d['farmer_item_id']
        return o


