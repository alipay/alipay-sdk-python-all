#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ForwardOrderInfo(object):

    def __init__(self):
        self._description = None
        self._order_create_time = None
        self._order_type = None
        self._out_order_expect_time = None
        self._self_order_expect_time = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_expect_time(self):
        return self._out_order_expect_time

    @out_order_expect_time.setter
    def out_order_expect_time(self, value):
        self._out_order_expect_time = value
    @property
    def self_order_expect_time(self):
        return self._self_order_expect_time

    @self_order_expect_time.setter
    def self_order_expect_time(self, value):
        self._self_order_expect_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_expect_time:
            if hasattr(self.out_order_expect_time, 'to_alipay_dict'):
                params['out_order_expect_time'] = self.out_order_expect_time.to_alipay_dict()
            else:
                params['out_order_expect_time'] = self.out_order_expect_time
        if self.self_order_expect_time:
            if hasattr(self.self_order_expect_time, 'to_alipay_dict'):
                params['self_order_expect_time'] = self.self_order_expect_time.to_alipay_dict()
            else:
                params['self_order_expect_time'] = self.self_order_expect_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ForwardOrderInfo()
        if 'description' in d:
            o.description = d['description']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_expect_time' in d:
            o.out_order_expect_time = d['out_order_expect_time']
        if 'self_order_expect_time' in d:
            o.self_order_expect_time = d['self_order_expect_time']
        return o


