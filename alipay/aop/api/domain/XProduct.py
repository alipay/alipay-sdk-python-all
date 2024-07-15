#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XProduct(object):

    def __init__(self):
        self._appoint_policy = None
        self._booking_phone = None
        self._capacity = None
        self._quantity = None
        self._reception_times = None
        self._type_name = None
        self._x_product_id = None
        self._x_product_name = None

    @property
    def appoint_policy(self):
        return self._appoint_policy

    @appoint_policy.setter
    def appoint_policy(self, value):
        self._appoint_policy = value
    @property
    def booking_phone(self):
        return self._booking_phone

    @booking_phone.setter
    def booking_phone(self, value):
        self._booking_phone = value
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def reception_times(self):
        return self._reception_times

    @reception_times.setter
    def reception_times(self, value):
        self._reception_times = value
    @property
    def type_name(self):
        return self._type_name

    @type_name.setter
    def type_name(self, value):
        self._type_name = value
    @property
    def x_product_id(self):
        return self._x_product_id

    @x_product_id.setter
    def x_product_id(self, value):
        self._x_product_id = value
    @property
    def x_product_name(self):
        return self._x_product_name

    @x_product_name.setter
    def x_product_name(self, value):
        self._x_product_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_policy:
            if hasattr(self.appoint_policy, 'to_alipay_dict'):
                params['appoint_policy'] = self.appoint_policy.to_alipay_dict()
            else:
                params['appoint_policy'] = self.appoint_policy
        if self.booking_phone:
            if hasattr(self.booking_phone, 'to_alipay_dict'):
                params['booking_phone'] = self.booking_phone.to_alipay_dict()
            else:
                params['booking_phone'] = self.booking_phone
        if self.capacity:
            if hasattr(self.capacity, 'to_alipay_dict'):
                params['capacity'] = self.capacity.to_alipay_dict()
            else:
                params['capacity'] = self.capacity
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.reception_times:
            if hasattr(self.reception_times, 'to_alipay_dict'):
                params['reception_times'] = self.reception_times.to_alipay_dict()
            else:
                params['reception_times'] = self.reception_times
        if self.type_name:
            if hasattr(self.type_name, 'to_alipay_dict'):
                params['type_name'] = self.type_name.to_alipay_dict()
            else:
                params['type_name'] = self.type_name
        if self.x_product_id:
            if hasattr(self.x_product_id, 'to_alipay_dict'):
                params['x_product_id'] = self.x_product_id.to_alipay_dict()
            else:
                params['x_product_id'] = self.x_product_id
        if self.x_product_name:
            if hasattr(self.x_product_name, 'to_alipay_dict'):
                params['x_product_name'] = self.x_product_name.to_alipay_dict()
            else:
                params['x_product_name'] = self.x_product_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XProduct()
        if 'appoint_policy' in d:
            o.appoint_policy = d['appoint_policy']
        if 'booking_phone' in d:
            o.booking_phone = d['booking_phone']
        if 'capacity' in d:
            o.capacity = d['capacity']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'reception_times' in d:
            o.reception_times = d['reception_times']
        if 'type_name' in d:
            o.type_name = d['type_name']
        if 'x_product_id' in d:
            o.x_product_id = d['x_product_id']
        if 'x_product_name' in d:
            o.x_product_name = d['x_product_name']
        return o


