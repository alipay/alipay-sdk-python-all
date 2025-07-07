#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsOrderModifyDTO(object):

    def __init__(self):
        self._delivery_id = None
        self._original_delivery_id = None
        self._original_waybill_id = None
        self._waybill_id = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def original_delivery_id(self):
        return self._original_delivery_id

    @original_delivery_id.setter
    def original_delivery_id(self, value):
        self._original_delivery_id = value
    @property
    def original_waybill_id(self):
        return self._original_waybill_id

    @original_waybill_id.setter
    def original_waybill_id(self, value):
        self._original_waybill_id = value
    @property
    def waybill_id(self):
        return self._waybill_id

    @waybill_id.setter
    def waybill_id(self, value):
        self._waybill_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
        if self.original_delivery_id:
            if hasattr(self.original_delivery_id, 'to_alipay_dict'):
                params['original_delivery_id'] = self.original_delivery_id.to_alipay_dict()
            else:
                params['original_delivery_id'] = self.original_delivery_id
        if self.original_waybill_id:
            if hasattr(self.original_waybill_id, 'to_alipay_dict'):
                params['original_waybill_id'] = self.original_waybill_id.to_alipay_dict()
            else:
                params['original_waybill_id'] = self.original_waybill_id
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
        o = LogisticsOrderModifyDTO()
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'original_delivery_id' in d:
            o.original_delivery_id = d['original_delivery_id']
        if 'original_waybill_id' in d:
            o.original_waybill_id = d['original_waybill_id']
        if 'waybill_id' in d:
            o.waybill_id = d['waybill_id']
        return o


