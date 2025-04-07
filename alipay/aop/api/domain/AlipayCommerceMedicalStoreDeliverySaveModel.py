#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Delivery import Delivery


class AlipayCommerceMedicalStoreDeliverySaveModel(object):

    def __init__(self):
        self._delivery_area = None
        self._store_code = None

    @property
    def delivery_area(self):
        return self._delivery_area

    @delivery_area.setter
    def delivery_area(self, value):
        if isinstance(value, Delivery):
            self._delivery_area = value
        else:
            self._delivery_area = Delivery.from_alipay_dict(value)
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_area:
            if hasattr(self.delivery_area, 'to_alipay_dict'):
                params['delivery_area'] = self.delivery_area.to_alipay_dict()
            else:
                params['delivery_area'] = self.delivery_area
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalStoreDeliverySaveModel()
        if 'delivery_area' in d:
            o.delivery_area = d['delivery_area']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


