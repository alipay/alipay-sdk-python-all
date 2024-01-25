#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryReceiveDTO(object):

    def __init__(self):
        self._logistics_order_id = None
        self._waybill_id = None

    @property
    def logistics_order_id(self):
        return self._logistics_order_id

    @logistics_order_id.setter
    def logistics_order_id(self, value):
        self._logistics_order_id = value
    @property
    def waybill_id(self):
        return self._waybill_id

    @waybill_id.setter
    def waybill_id(self, value):
        self._waybill_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_order_id:
            if hasattr(self.logistics_order_id, 'to_alipay_dict'):
                params['logistics_order_id'] = self.logistics_order_id.to_alipay_dict()
            else:
                params['logistics_order_id'] = self.logistics_order_id
        if self.waybill_id:
            if hasattr(self.waybill_id, 'to_alipay_dict'):
                params['waybill_id'] = self.waybill_id.to_alipay_dict()
            else:
                params['waybill_id'] = self.waybill_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryReceiveDTO()
        if 'logistics_order_id' in d:
            o.logistics_order_id = d['logistics_order_id']
        if 'waybill_id' in d:
            o.waybill_id = d['waybill_id']
        return o


