#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingCardbarcodeCreateModel(object):

    def __init__(self):
        self._equipment_id = None
        self._parking_id = None

    @property
    def equipment_id(self):
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, value):
        self._equipment_id = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.equipment_id:
            if hasattr(self.equipment_id, 'to_alipay_dict'):
                params['equipment_id'] = self.equipment_id.to_alipay_dict()
            else:
                params['equipment_id'] = self.equipment_id
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingCardbarcodeCreateModel()
        if 'equipment_id' in d:
            o.equipment_id = d['equipment_id']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        return o


