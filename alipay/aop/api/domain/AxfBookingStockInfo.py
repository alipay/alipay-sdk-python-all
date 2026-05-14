#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfBookingStockInfo(object):

    def __init__(self):
        self._available_quantity = None
        self._status = None
        self._time = None

    @property
    def available_quantity(self):
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, value):
        self._available_quantity = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_quantity:
            if hasattr(self.available_quantity, 'to_alipay_dict'):
                params['available_quantity'] = self.available_quantity.to_alipay_dict()
            else:
                params['available_quantity'] = self.available_quantity
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfBookingStockInfo()
        if 'available_quantity' in d:
            o.available_quantity = d['available_quantity']
        if 'status' in d:
            o.status = d['status']
        if 'time' in d:
            o.time = d['time']
        return o


