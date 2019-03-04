#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpSceneRatingApplyModel(object):

    def __init__(self):
        self._apply_environment = None
        self._order_no = None
        self._out_order_no = None

    @property
    def apply_environment(self):
        return self._apply_environment

    @apply_environment.setter
    def apply_environment(self, value):
        self._apply_environment = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_environment:
            if hasattr(self.apply_environment, 'to_alipay_dict'):
                params['apply_environment'] = self.apply_environment.to_alipay_dict()
            else:
                params['apply_environment'] = self.apply_environment
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpSceneRatingApplyModel()
        if 'apply_environment' in d:
            o.apply_environment = d['apply_environment']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


