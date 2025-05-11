#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryPointDTO import DeliveryPointDTO


class AlipayCommerceMedicalStoreDeliverySyncModel(object):

    def __init__(self):
        self._delivery_area_list = None
        self._store_code = None

    @property
    def delivery_area_list(self):
        return self._delivery_area_list

    @delivery_area_list.setter
    def delivery_area_list(self, value):
        if isinstance(value, list):
            self._delivery_area_list = list()
            for i in value:
                if isinstance(i, DeliveryPointDTO):
                    self._delivery_area_list.append(i)
                else:
                    self._delivery_area_list.append(DeliveryPointDTO.from_alipay_dict(i))
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_area_list:
            if isinstance(self.delivery_area_list, list):
                for i in range(0, len(self.delivery_area_list)):
                    element = self.delivery_area_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_area_list[i] = element.to_alipay_dict()
            if hasattr(self.delivery_area_list, 'to_alipay_dict'):
                params['delivery_area_list'] = self.delivery_area_list.to_alipay_dict()
            else:
                params['delivery_area_list'] = self.delivery_area_list
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
        o = AlipayCommerceMedicalStoreDeliverySyncModel()
        if 'delivery_area_list' in d:
            o.delivery_area_list = d['delivery_area_list']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


