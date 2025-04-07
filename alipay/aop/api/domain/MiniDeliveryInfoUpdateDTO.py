#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniDeliveryInfoUpdateDTO(object):

    def __init__(self):
        self._delivery_end_time = None
        self._delivery_start_time = None

    @property
    def delivery_end_time(self):
        return self._delivery_end_time

    @delivery_end_time.setter
    def delivery_end_time(self, value):
        self._delivery_end_time = value
    @property
    def delivery_start_time(self):
        return self._delivery_start_time

    @delivery_start_time.setter
    def delivery_start_time(self, value):
        self._delivery_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_end_time:
            if hasattr(self.delivery_end_time, 'to_alipay_dict'):
                params['delivery_end_time'] = self.delivery_end_time.to_alipay_dict()
            else:
                params['delivery_end_time'] = self.delivery_end_time
        if self.delivery_start_time:
            if hasattr(self.delivery_start_time, 'to_alipay_dict'):
                params['delivery_start_time'] = self.delivery_start_time.to_alipay_dict()
            else:
                params['delivery_start_time'] = self.delivery_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniDeliveryInfoUpdateDTO()
        if 'delivery_end_time' in d:
            o.delivery_end_time = d['delivery_end_time']
        if 'delivery_start_time' in d:
            o.delivery_start_time = d['delivery_start_time']
        return o


