#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SellerSyncRentOrderExtInfo(object):

    def __init__(self):
        self._order_sign_price = None
        self._order_type = None
        self._rent_end_time = None
        self._rent_mode = None
        self._rent_start_time = None

    @property
    def order_sign_price(self):
        return self._order_sign_price

    @order_sign_price.setter
    def order_sign_price(self, value):
        self._order_sign_price = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def rent_end_time(self):
        return self._rent_end_time

    @rent_end_time.setter
    def rent_end_time(self, value):
        self._rent_end_time = value
    @property
    def rent_mode(self):
        return self._rent_mode

    @rent_mode.setter
    def rent_mode(self, value):
        self._rent_mode = value
    @property
    def rent_start_time(self):
        return self._rent_start_time

    @rent_start_time.setter
    def rent_start_time(self, value):
        self._rent_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_sign_price:
            if hasattr(self.order_sign_price, 'to_alipay_dict'):
                params['order_sign_price'] = self.order_sign_price.to_alipay_dict()
            else:
                params['order_sign_price'] = self.order_sign_price
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.rent_end_time:
            if hasattr(self.rent_end_time, 'to_alipay_dict'):
                params['rent_end_time'] = self.rent_end_time.to_alipay_dict()
            else:
                params['rent_end_time'] = self.rent_end_time
        if self.rent_mode:
            if hasattr(self.rent_mode, 'to_alipay_dict'):
                params['rent_mode'] = self.rent_mode.to_alipay_dict()
            else:
                params['rent_mode'] = self.rent_mode
        if self.rent_start_time:
            if hasattr(self.rent_start_time, 'to_alipay_dict'):
                params['rent_start_time'] = self.rent_start_time.to_alipay_dict()
            else:
                params['rent_start_time'] = self.rent_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SellerSyncRentOrderExtInfo()
        if 'order_sign_price' in d:
            o.order_sign_price = d['order_sign_price']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'rent_end_time' in d:
            o.rent_end_time = d['rent_end_time']
        if 'rent_mode' in d:
            o.rent_mode = d['rent_mode']
        if 'rent_start_time' in d:
            o.rent_start_time = d['rent_start_time']
        return o


