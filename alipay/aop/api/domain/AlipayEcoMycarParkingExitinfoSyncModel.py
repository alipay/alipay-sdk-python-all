#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingExitinfoSyncModel(object):

    def __init__(self):
        self._actual_amount = None
        self._car_color = None
        self._car_number = None
        self._discount_amount = None
        self._exit_id = None
        self._is_encrypt_car_number = None
        self._isv_url = None
        self._order_amount = None
        self._out_serial_no = None
        self._out_time = None
        self._parking_id = None
        self._serial_no = None
        self._space_number = None
        self._store_id = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def car_color(self):
        return self._car_color

    @car_color.setter
    def car_color(self, value):
        self._car_color = value
    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def exit_id(self):
        return self._exit_id

    @exit_id.setter
    def exit_id(self, value):
        self._exit_id = value
    @property
    def is_encrypt_car_number(self):
        return self._is_encrypt_car_number

    @is_encrypt_car_number.setter
    def is_encrypt_car_number(self, value):
        self._is_encrypt_car_number = value
    @property
    def isv_url(self):
        return self._isv_url

    @isv_url.setter
    def isv_url(self, value):
        self._isv_url = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def out_time(self):
        return self._out_time

    @out_time.setter
    def out_time(self, value):
        self._out_time = value
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
    @property
    def space_number(self):
        return self._space_number

    @space_number.setter
    def space_number(self, value):
        self._space_number = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.car_color:
            if hasattr(self.car_color, 'to_alipay_dict'):
                params['car_color'] = self.car_color.to_alipay_dict()
            else:
                params['car_color'] = self.car_color
        if self.car_number:
            if hasattr(self.car_number, 'to_alipay_dict'):
                params['car_number'] = self.car_number.to_alipay_dict()
            else:
                params['car_number'] = self.car_number
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.exit_id:
            if hasattr(self.exit_id, 'to_alipay_dict'):
                params['exit_id'] = self.exit_id.to_alipay_dict()
            else:
                params['exit_id'] = self.exit_id
        if self.is_encrypt_car_number:
            if hasattr(self.is_encrypt_car_number, 'to_alipay_dict'):
                params['is_encrypt_car_number'] = self.is_encrypt_car_number.to_alipay_dict()
            else:
                params['is_encrypt_car_number'] = self.is_encrypt_car_number
        if self.isv_url:
            if hasattr(self.isv_url, 'to_alipay_dict'):
                params['isv_url'] = self.isv_url.to_alipay_dict()
            else:
                params['isv_url'] = self.isv_url
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.out_time:
            if hasattr(self.out_time, 'to_alipay_dict'):
                params['out_time'] = self.out_time.to_alipay_dict()
            else:
                params['out_time'] = self.out_time
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
        if self.space_number:
            if hasattr(self.space_number, 'to_alipay_dict'):
                params['space_number'] = self.space_number.to_alipay_dict()
            else:
                params['space_number'] = self.space_number
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingExitinfoSyncModel()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'car_color' in d:
            o.car_color = d['car_color']
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'exit_id' in d:
            o.exit_id = d['exit_id']
        if 'is_encrypt_car_number' in d:
            o.is_encrypt_car_number = d['is_encrypt_car_number']
        if 'isv_url' in d:
            o.isv_url = d['isv_url']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'out_time' in d:
            o.out_time = d['out_time']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'space_number' in d:
            o.space_number = d['space_number']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


