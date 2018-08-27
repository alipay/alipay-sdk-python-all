#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingCardidQueryModel(object):

    def __init__(self):
        self._car_number = None
        self._parking_id = None
        self._sel_time = None
        self._transaction_no = None

    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def sel_time(self):
        return self._sel_time

    @sel_time.setter
    def sel_time(self, value):
        self._sel_time = value
    @property
    def transaction_no(self):
        return self._transaction_no

    @transaction_no.setter
    def transaction_no(self, value):
        self._transaction_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_number:
            if hasattr(self.car_number, 'to_alipay_dict'):
                params['car_number'] = self.car_number.to_alipay_dict()
            else:
                params['car_number'] = self.car_number
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.sel_time:
            if hasattr(self.sel_time, 'to_alipay_dict'):
                params['sel_time'] = self.sel_time.to_alipay_dict()
            else:
                params['sel_time'] = self.sel_time
        if self.transaction_no:
            if hasattr(self.transaction_no, 'to_alipay_dict'):
                params['transaction_no'] = self.transaction_no.to_alipay_dict()
            else:
                params['transaction_no'] = self.transaction_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingCardidQueryModel()
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'sel_time' in d:
            o.sel_time = d['sel_time']
        if 'transaction_no' in d:
            o.transaction_no = d['transaction_no']
        return o


