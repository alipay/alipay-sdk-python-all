#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingCharginginfoSyncModel(object):

    def __init__(self):
        self._car_number = None
        self._isv_url = None
        self._parking_id = None
        self._serial_no = None

    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value
    @property
    def isv_url(self):
        return self._isv_url

    @isv_url.setter
    def isv_url(self, value):
        self._isv_url = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_number:
            if hasattr(self.car_number, 'to_alipay_dict'):
                params['car_number'] = self.car_number.to_alipay_dict()
            else:
                params['car_number'] = self.car_number
        if self.isv_url:
            if hasattr(self.isv_url, 'to_alipay_dict'):
                params['isv_url'] = self.isv_url.to_alipay_dict()
            else:
                params['isv_url'] = self.isv_url
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingCharginginfoSyncModel()
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'isv_url' in d:
            o.isv_url = d['isv_url']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        return o


