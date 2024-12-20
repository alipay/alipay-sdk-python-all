#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceItaskOutorderPrivacyphoneQueryModel(object):

    def __init__(self):
        self._out_order_id = None
        self._self_order_id = None

    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def self_order_id(self):
        return self._self_order_id

    @self_order_id.setter
    def self_order_id(self, value):
        self._self_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.self_order_id:
            if hasattr(self.self_order_id, 'to_alipay_dict'):
                params['self_order_id'] = self.self_order_id.to_alipay_dict()
            else:
                params['self_order_id'] = self.self_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskOutorderPrivacyphoneQueryModel()
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'self_order_id' in d:
            o.self_order_id = d['self_order_id']
        return o


