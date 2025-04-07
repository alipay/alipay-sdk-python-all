#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Delivery import Delivery
from alipay.aop.api.domain.EffectivePeriodDTO import EffectivePeriodDTO


class AlipayCommerceMedicalStoreDeliveryspecialSaveModel(object):

    def __init__(self):
        self._delivery_area = None
        self._delivery_time = None
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
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        if isinstance(value, EffectivePeriodDTO):
            self._delivery_time = value
        else:
            self._delivery_time = EffectivePeriodDTO.from_alipay_dict(value)
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
        if self.delivery_time:
            if hasattr(self.delivery_time, 'to_alipay_dict'):
                params['delivery_time'] = self.delivery_time.to_alipay_dict()
            else:
                params['delivery_time'] = self.delivery_time
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
        o = AlipayCommerceMedicalStoreDeliveryspecialSaveModel()
        if 'delivery_area' in d:
            o.delivery_area = d['delivery_area']
        if 'delivery_time' in d:
            o.delivery_time = d['delivery_time']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


