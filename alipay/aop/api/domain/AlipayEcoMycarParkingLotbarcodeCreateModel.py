#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingLotbarcodeCreateModel(object):

    def __init__(self):
        self._parking_id = None

    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayEcoMycarParkingLotbarcodeCreateModel()
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        return o


