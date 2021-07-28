#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmpeDeviceVO(object):

    def __init__(self):
        self._add_time = None
        self._device_id = None
        self._model_id = None
        self._model_name = None
        self._model_no = None
        self._product_id = None
        self._product_name = None

    @property
    def add_time(self):
        return self._add_time

    @add_time.setter
    def add_time(self, value):
        self._add_time = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
    @property
    def model_no(self):
        return self._model_no

    @model_no.setter
    def model_no(self, value):
        self._model_no = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_time:
            if hasattr(self.add_time, 'to_alipay_dict'):
                params['add_time'] = self.add_time.to_alipay_dict()
            else:
                params['add_time'] = self.add_time
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
        if self.model_no:
            if hasattr(self.model_no, 'to_alipay_dict'):
                params['model_no'] = self.model_no.to_alipay_dict()
            else:
                params['model_no'] = self.model_no
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmpeDeviceVO()
        if 'add_time' in d:
            o.add_time = d['add_time']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'model_name' in d:
            o.model_name = d['model_name']
        if 'model_no' in d:
            o.model_no = d['model_no']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        return o


