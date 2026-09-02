#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentProcurementOrderQueryModel(object):

    def __init__(self):
        self._out_procurement_order_id = None
        self._procurement_order_id = None

    @property
    def out_procurement_order_id(self):
        return self._out_procurement_order_id

    @out_procurement_order_id.setter
    def out_procurement_order_id(self, value):
        self._out_procurement_order_id = value
    @property
    def procurement_order_id(self):
        return self._procurement_order_id

    @procurement_order_id.setter
    def procurement_order_id(self, value):
        self._procurement_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_procurement_order_id:
            if hasattr(self.out_procurement_order_id, 'to_alipay_dict'):
                params['out_procurement_order_id'] = self.out_procurement_order_id.to_alipay_dict()
            else:
                params['out_procurement_order_id'] = self.out_procurement_order_id
        if self.procurement_order_id:
            if hasattr(self.procurement_order_id, 'to_alipay_dict'):
                params['procurement_order_id'] = self.procurement_order_id.to_alipay_dict()
            else:
                params['procurement_order_id'] = self.procurement_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentProcurementOrderQueryModel()
        if 'out_procurement_order_id' in d:
            o.out_procurement_order_id = d['out_procurement_order_id']
        if 'procurement_order_id' in d:
            o.procurement_order_id = d['procurement_order_id']
        return o


