#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotPointDeleteModel(object):

    def __init__(self):
        self._out_device_point_id = None

    @property
    def out_device_point_id(self):
        return self._out_device_point_id

    @out_device_point_id.setter
    def out_device_point_id(self, value):
        self._out_device_point_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_device_point_id:
            if hasattr(self.out_device_point_id, 'to_alipay_dict'):
                params['out_device_point_id'] = self.out_device_point_id.to_alipay_dict()
            else:
                params['out_device_point_id'] = self.out_device_point_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotPointDeleteModel()
        if 'out_device_point_id' in d:
            o.out_device_point_id = d['out_device_point_id']
        return o


