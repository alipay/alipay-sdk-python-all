#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentProcurementInfoVO(object):

    def __init__(self):
        self._procurement_order_id = None

    @property
    def procurement_order_id(self):
        return self._procurement_order_id

    @procurement_order_id.setter
    def procurement_order_id(self, value):
        self._procurement_order_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = RentProcurementInfoVO()
        if 'procurement_order_id' in d:
            o.procurement_order_id = d['procurement_order_id']
        return o


