#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosDiscountDetail(object):

    def __init__(self):
        self._discount_name = None
        self._discount_type = None
        self._ext_info = None
        self._mrt_discount = None
        self._rt_discount = None

    @property
    def discount_name(self):
        return self._discount_name

    @discount_name.setter
    def discount_name(self, value):
        self._discount_name = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def mrt_discount(self):
        return self._mrt_discount

    @mrt_discount.setter
    def mrt_discount(self, value):
        self._mrt_discount = value
    @property
    def rt_discount(self):
        return self._rt_discount

    @rt_discount.setter
    def rt_discount(self, value):
        self._rt_discount = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_name:
            if hasattr(self.discount_name, 'to_alipay_dict'):
                params['discount_name'] = self.discount_name.to_alipay_dict()
            else:
                params['discount_name'] = self.discount_name
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.mrt_discount:
            if hasattr(self.mrt_discount, 'to_alipay_dict'):
                params['mrt_discount'] = self.mrt_discount.to_alipay_dict()
            else:
                params['mrt_discount'] = self.mrt_discount
        if self.rt_discount:
            if hasattr(self.rt_discount, 'to_alipay_dict'):
                params['rt_discount'] = self.rt_discount.to_alipay_dict()
            else:
                params['rt_discount'] = self.rt_discount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosDiscountDetail()
        if 'discount_name' in d:
            o.discount_name = d['discount_name']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'mrt_discount' in d:
            o.mrt_discount = d['mrt_discount']
        if 'rt_discount' in d:
            o.rt_discount = d['rt_discount']
        return o


