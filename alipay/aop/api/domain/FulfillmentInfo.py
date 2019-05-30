#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FulfillmentInfo(object):

    def __init__(self):
        self._biz_ext_param = None
        self._biz_time = None
        self._out_order_no = None

    @property
    def biz_ext_param(self):
        return self._biz_ext_param

    @biz_ext_param.setter
    def biz_ext_param(self, value):
        self._biz_ext_param = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_ext_param:
            if hasattr(self.biz_ext_param, 'to_alipay_dict'):
                params['biz_ext_param'] = self.biz_ext_param.to_alipay_dict()
            else:
                params['biz_ext_param'] = self.biz_ext_param
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
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
        o = FulfillmentInfo()
        if 'biz_ext_param' in d:
            o.biz_ext_param = d['biz_ext_param']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


