#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceFarmerDeleteModel(object):

    def __init__(self):
        self._farmer_id = None

    @property
    def farmer_id(self):
        return self._farmer_id

    @farmer_id.setter
    def farmer_id(self, value):
        self._farmer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.farmer_id:
            if hasattr(self.farmer_id, 'to_alipay_dict'):
                params['farmer_id'] = self.farmer_id.to_alipay_dict()
            else:
                params['farmer_id'] = self.farmer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceFarmerDeleteModel()
        if 'farmer_id' in d:
            o.farmer_id = d['farmer_id']
        return o


