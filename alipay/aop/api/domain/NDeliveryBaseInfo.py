#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NDeliveryBaseInfo(object):

    def __init__(self):
        self._n_delivery_begin_time = None
        self._n_delivery_end_time = None
        self._n_delivery_name = None

    @property
    def n_delivery_begin_time(self):
        return self._n_delivery_begin_time

    @n_delivery_begin_time.setter
    def n_delivery_begin_time(self, value):
        self._n_delivery_begin_time = value
    @property
    def n_delivery_end_time(self):
        return self._n_delivery_end_time

    @n_delivery_end_time.setter
    def n_delivery_end_time(self, value):
        self._n_delivery_end_time = value
    @property
    def n_delivery_name(self):
        return self._n_delivery_name

    @n_delivery_name.setter
    def n_delivery_name(self, value):
        self._n_delivery_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.n_delivery_begin_time:
            if hasattr(self.n_delivery_begin_time, 'to_alipay_dict'):
                params['n_delivery_begin_time'] = self.n_delivery_begin_time.to_alipay_dict()
            else:
                params['n_delivery_begin_time'] = self.n_delivery_begin_time
        if self.n_delivery_end_time:
            if hasattr(self.n_delivery_end_time, 'to_alipay_dict'):
                params['n_delivery_end_time'] = self.n_delivery_end_time.to_alipay_dict()
            else:
                params['n_delivery_end_time'] = self.n_delivery_end_time
        if self.n_delivery_name:
            if hasattr(self.n_delivery_name, 'to_alipay_dict'):
                params['n_delivery_name'] = self.n_delivery_name.to_alipay_dict()
            else:
                params['n_delivery_name'] = self.n_delivery_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeliveryBaseInfo()
        if 'n_delivery_begin_time' in d:
            o.n_delivery_begin_time = d['n_delivery_begin_time']
        if 'n_delivery_end_time' in d:
            o.n_delivery_end_time = d['n_delivery_end_time']
        if 'n_delivery_name' in d:
            o.n_delivery_name = d['n_delivery_name']
        return o


