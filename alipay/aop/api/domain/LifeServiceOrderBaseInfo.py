#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeServiceOrderBaseInfo(object):

    def __init__(self):
        self._merchant_order_id = None
        self._order_create_time = None
        self._order_status = None
        self._order_type = None

    @property
    def merchant_order_id(self):
        return self._merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self._merchant_order_id = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_order_id:
            if hasattr(self.merchant_order_id, 'to_alipay_dict'):
                params['merchant_order_id'] = self.merchant_order_id.to_alipay_dict()
            else:
                params['merchant_order_id'] = self.merchant_order_id
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceOrderBaseInfo()
        if 'merchant_order_id' in d:
            o.merchant_order_id = d['merchant_order_id']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        return o


