#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentHouseEquipmentVO(object):

    def __init__(self):
        self._customize = None
        self._equipment = None
        self._size = None

    @property
    def customize(self):
        return self._customize

    @customize.setter
    def customize(self, value):
        self._customize = value
    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, value):
        self._equipment = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


    def to_alipay_dict(self):
        params = dict()
        if self.customize:
            if hasattr(self.customize, 'to_alipay_dict'):
                params['customize'] = self.customize.to_alipay_dict()
            else:
                params['customize'] = self.customize
        if self.equipment:
            if hasattr(self.equipment, 'to_alipay_dict'):
                params['equipment'] = self.equipment.to_alipay_dict()
            else:
                params['equipment'] = self.equipment
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentHouseEquipmentVO()
        if 'customize' in d:
            o.customize = d['customize']
        if 'equipment' in d:
            o.equipment = d['equipment']
        if 'size' in d:
            o.size = d['size']
        return o


