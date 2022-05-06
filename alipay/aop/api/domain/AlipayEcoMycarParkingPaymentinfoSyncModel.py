#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingPaymentinfoSyncModel(object):

    def __init__(self):
        self._car_number = None
        self._isv_url = None
        self._out_serial_no = None
        self._parking_id = None
        self._payment_free_minutes = None
        self._payment_time = None
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
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def payment_free_minutes(self):
        return self._payment_free_minutes

    @payment_free_minutes.setter
    def payment_free_minutes(self, value):
        self._payment_free_minutes = value
    @property
    def payment_time(self):
        return self._payment_time

    @payment_time.setter
    def payment_time(self, value):
        self._payment_time = value
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
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.payment_free_minutes:
            if hasattr(self.payment_free_minutes, 'to_alipay_dict'):
                params['payment_free_minutes'] = self.payment_free_minutes.to_alipay_dict()
            else:
                params['payment_free_minutes'] = self.payment_free_minutes
        if self.payment_time:
            if hasattr(self.payment_time, 'to_alipay_dict'):
                params['payment_time'] = self.payment_time.to_alipay_dict()
            else:
                params['payment_time'] = self.payment_time
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
        o = AlipayEcoMycarParkingPaymentinfoSyncModel()
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'isv_url' in d:
            o.isv_url = d['isv_url']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'payment_free_minutes' in d:
            o.payment_free_minutes = d['payment_free_minutes']
        if 'payment_time' in d:
            o.payment_time = d['payment_time']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        return o


