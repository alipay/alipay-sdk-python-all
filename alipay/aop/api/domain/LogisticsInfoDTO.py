#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsInfoDTO(object):

    def __init__(self):
        self._delivery_time = None
        self._delivery_type = None

    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        self._delivery_time = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_time:
            if hasattr(self.delivery_time, 'to_alipay_dict'):
                params['delivery_time'] = self.delivery_time.to_alipay_dict()
            else:
                params['delivery_time'] = self.delivery_time
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsInfoDTO()
        if 'delivery_time' in d:
            o.delivery_time = d['delivery_time']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        return o


