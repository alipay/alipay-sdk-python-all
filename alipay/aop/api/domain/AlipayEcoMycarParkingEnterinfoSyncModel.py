#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingEnterinfoSyncModel(object):

    def __init__(self):
        self._agreement_query = None
        self._car_color = None
        self._car_number = None
        self._entrance_id = None
        self._free_minutes = None
        self._in_time = None
        self._is_encrypt_car_number = None
        self._isv_url = None
        self._out_serial_no = None
        self._parking_id = None
        self._space_number = None
        self._store_id = None

    @property
    def agreement_query(self):
        return self._agreement_query

    @agreement_query.setter
    def agreement_query(self, value):
        self._agreement_query = value
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
    def entrance_id(self):
        return self._entrance_id

    @entrance_id.setter
    def entrance_id(self, value):
        self._entrance_id = value
    @property
    def free_minutes(self):
        return self._free_minutes

    @free_minutes.setter
    def free_minutes(self, value):
        self._free_minutes = value
    @property
    def in_time(self):
        return self._in_time

    @in_time.setter
    def in_time(self, value):
        self._in_time = value
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
        if self.agreement_query:
            if hasattr(self.agreement_query, 'to_alipay_dict'):
                params['agreement_query'] = self.agreement_query.to_alipay_dict()
            else:
                params['agreement_query'] = self.agreement_query
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
        if self.entrance_id:
            if hasattr(self.entrance_id, 'to_alipay_dict'):
                params['entrance_id'] = self.entrance_id.to_alipay_dict()
            else:
                params['entrance_id'] = self.entrance_id
        if self.free_minutes:
            if hasattr(self.free_minutes, 'to_alipay_dict'):
                params['free_minutes'] = self.free_minutes.to_alipay_dict()
            else:
                params['free_minutes'] = self.free_minutes
        if self.in_time:
            if hasattr(self.in_time, 'to_alipay_dict'):
                params['in_time'] = self.in_time.to_alipay_dict()
            else:
                params['in_time'] = self.in_time
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
        o = AlipayEcoMycarParkingEnterinfoSyncModel()
        if 'agreement_query' in d:
            o.agreement_query = d['agreement_query']
        if 'car_color' in d:
            o.car_color = d['car_color']
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'entrance_id' in d:
            o.entrance_id = d['entrance_id']
        if 'free_minutes' in d:
            o.free_minutes = d['free_minutes']
        if 'in_time' in d:
            o.in_time = d['in_time']
        if 'is_encrypt_car_number' in d:
            o.is_encrypt_car_number = d['is_encrypt_car_number']
        if 'isv_url' in d:
            o.isv_url = d['isv_url']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'space_number' in d:
            o.space_number = d['space_number']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


