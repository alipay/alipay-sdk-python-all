#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EquipmentBindInfo(object):

    def __init__(self):
        self._equipment_id = None
        self._is_bind_shop = None

    @property
    def equipment_id(self):
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, value):
        self._equipment_id = value
    @property
    def is_bind_shop(self):
        return self._is_bind_shop

    @is_bind_shop.setter
    def is_bind_shop(self, value):
        self._is_bind_shop = value


    def to_alipay_dict(self):
        params = dict()
        if self.equipment_id:
            if hasattr(self.equipment_id, 'to_alipay_dict'):
                params['equipment_id'] = self.equipment_id.to_alipay_dict()
            else:
                params['equipment_id'] = self.equipment_id
        if self.is_bind_shop:
            if hasattr(self.is_bind_shop, 'to_alipay_dict'):
                params['is_bind_shop'] = self.is_bind_shop.to_alipay_dict()
            else:
                params['is_bind_shop'] = self.is_bind_shop
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EquipmentBindInfo()
        if 'equipment_id' in d:
            o.equipment_id = d['equipment_id']
        if 'is_bind_shop' in d:
            o.is_bind_shop = d['is_bind_shop']
        return o


