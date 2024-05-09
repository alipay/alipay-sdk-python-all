#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AftersaleLogisticsInfoDTO(object):

    def __init__(self):
        self._delivery_id = None
        self._waybill_id = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
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
        o = AftersaleLogisticsInfoDTO()
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'waybill_id' in d:
            o.waybill_id = d['waybill_id']
        return o


