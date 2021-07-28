#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceOrderStatus(object):

    def __init__(self):
        self._device_order_status = None
        self._order_id = None
        self._order_type = None

    @property
    def device_order_status(self):
        return self._device_order_status

    @device_order_status.setter
    def device_order_status(self, value):
        self._device_order_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_order_status:
            if hasattr(self.device_order_status, 'to_alipay_dict'):
                params['device_order_status'] = self.device_order_status.to_alipay_dict()
            else:
                params['device_order_status'] = self.device_order_status
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
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
        o = DeviceOrderStatus()
        if 'device_order_status' in d:
            o.device_order_status = d['device_order_status']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        return o


