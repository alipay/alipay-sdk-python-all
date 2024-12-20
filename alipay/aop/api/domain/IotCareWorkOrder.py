#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotCareWorkOrder(object):

    def __init__(self):
        self._device_category_name = None
        self._new_device_sn = None
        self._sn = None
        self._worker_order_create_time = None
        self._worker_order_end_time = None
        self._worker_order_id = None

    @property
    def device_category_name(self):
        return self._device_category_name

    @device_category_name.setter
    def device_category_name(self, value):
        self._device_category_name = value
    @property
    def new_device_sn(self):
        return self._new_device_sn

    @new_device_sn.setter
    def new_device_sn(self, value):
        self._new_device_sn = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def worker_order_create_time(self):
        return self._worker_order_create_time

    @worker_order_create_time.setter
    def worker_order_create_time(self, value):
        self._worker_order_create_time = value
    @property
    def worker_order_end_time(self):
        return self._worker_order_end_time

    @worker_order_end_time.setter
    def worker_order_end_time(self, value):
        self._worker_order_end_time = value
    @property
    def worker_order_id(self):
        return self._worker_order_id

    @worker_order_id.setter
    def worker_order_id(self, value):
        self._worker_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_category_name:
            if hasattr(self.device_category_name, 'to_alipay_dict'):
                params['device_category_name'] = self.device_category_name.to_alipay_dict()
            else:
                params['device_category_name'] = self.device_category_name
        if self.new_device_sn:
            if hasattr(self.new_device_sn, 'to_alipay_dict'):
                params['new_device_sn'] = self.new_device_sn.to_alipay_dict()
            else:
                params['new_device_sn'] = self.new_device_sn
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.worker_order_create_time:
            if hasattr(self.worker_order_create_time, 'to_alipay_dict'):
                params['worker_order_create_time'] = self.worker_order_create_time.to_alipay_dict()
            else:
                params['worker_order_create_time'] = self.worker_order_create_time
        if self.worker_order_end_time:
            if hasattr(self.worker_order_end_time, 'to_alipay_dict'):
                params['worker_order_end_time'] = self.worker_order_end_time.to_alipay_dict()
            else:
                params['worker_order_end_time'] = self.worker_order_end_time
        if self.worker_order_id:
            if hasattr(self.worker_order_id, 'to_alipay_dict'):
                params['worker_order_id'] = self.worker_order_id.to_alipay_dict()
            else:
                params['worker_order_id'] = self.worker_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotCareWorkOrder()
        if 'device_category_name' in d:
            o.device_category_name = d['device_category_name']
        if 'new_device_sn' in d:
            o.new_device_sn = d['new_device_sn']
        if 'sn' in d:
            o.sn = d['sn']
        if 'worker_order_create_time' in d:
            o.worker_order_create_time = d['worker_order_create_time']
        if 'worker_order_end_time' in d:
            o.worker_order_end_time = d['worker_order_end_time']
        if 'worker_order_id' in d:
            o.worker_order_id = d['worker_order_id']
        return o


