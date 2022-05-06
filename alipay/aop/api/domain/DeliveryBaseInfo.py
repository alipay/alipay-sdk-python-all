#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryMaterial import DeliveryMaterial


class DeliveryBaseInfo(object):

    def __init__(self):
        self._delivery_begin_time = None
        self._delivery_end_time = None
        self._delivery_material = None
        self._delivery_name = None

    @property
    def delivery_begin_time(self):
        return self._delivery_begin_time

    @delivery_begin_time.setter
    def delivery_begin_time(self, value):
        self._delivery_begin_time = value
    @property
    def delivery_end_time(self):
        return self._delivery_end_time

    @delivery_end_time.setter
    def delivery_end_time(self, value):
        self._delivery_end_time = value
    @property
    def delivery_material(self):
        return self._delivery_material

    @delivery_material.setter
    def delivery_material(self, value):
        if isinstance(value, DeliveryMaterial):
            self._delivery_material = value
        else:
            self._delivery_material = DeliveryMaterial.from_alipay_dict(value)
    @property
    def delivery_name(self):
        return self._delivery_name

    @delivery_name.setter
    def delivery_name(self, value):
        self._delivery_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_begin_time:
            if hasattr(self.delivery_begin_time, 'to_alipay_dict'):
                params['delivery_begin_time'] = self.delivery_begin_time.to_alipay_dict()
            else:
                params['delivery_begin_time'] = self.delivery_begin_time
        if self.delivery_end_time:
            if hasattr(self.delivery_end_time, 'to_alipay_dict'):
                params['delivery_end_time'] = self.delivery_end_time.to_alipay_dict()
            else:
                params['delivery_end_time'] = self.delivery_end_time
        if self.delivery_material:
            if hasattr(self.delivery_material, 'to_alipay_dict'):
                params['delivery_material'] = self.delivery_material.to_alipay_dict()
            else:
                params['delivery_material'] = self.delivery_material
        if self.delivery_name:
            if hasattr(self.delivery_name, 'to_alipay_dict'):
                params['delivery_name'] = self.delivery_name.to_alipay_dict()
            else:
                params['delivery_name'] = self.delivery_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryBaseInfo()
        if 'delivery_begin_time' in d:
            o.delivery_begin_time = d['delivery_begin_time']
        if 'delivery_end_time' in d:
            o.delivery_end_time = d['delivery_end_time']
        if 'delivery_material' in d:
            o.delivery_material = d['delivery_material']
        if 'delivery_name' in d:
            o.delivery_name = d['delivery_name']
        return o


