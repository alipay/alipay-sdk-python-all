#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstallmentIntDiscountModel(object):

    def __init__(self):
        self._has_int_discount = None
        self._has_int_free = None
        self._install_num = None

    @property
    def has_int_discount(self):
        return self._has_int_discount

    @has_int_discount.setter
    def has_int_discount(self, value):
        self._has_int_discount = value
    @property
    def has_int_free(self):
        return self._has_int_free

    @has_int_free.setter
    def has_int_free(self, value):
        self._has_int_free = value
    @property
    def install_num(self):
        return self._install_num

    @install_num.setter
    def install_num(self, value):
        self._install_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_int_discount:
            if hasattr(self.has_int_discount, 'to_alipay_dict'):
                params['has_int_discount'] = self.has_int_discount.to_alipay_dict()
            else:
                params['has_int_discount'] = self.has_int_discount
        if self.has_int_free:
            if hasattr(self.has_int_free, 'to_alipay_dict'):
                params['has_int_free'] = self.has_int_free.to_alipay_dict()
            else:
                params['has_int_free'] = self.has_int_free
        if self.install_num:
            if hasattr(self.install_num, 'to_alipay_dict'):
                params['install_num'] = self.install_num.to_alipay_dict()
            else:
                params['install_num'] = self.install_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentIntDiscountModel()
        if 'has_int_discount' in d:
            o.has_int_discount = d['has_int_discount']
        if 'has_int_free' in d:
            o.has_int_free = d['has_int_free']
        if 'install_num' in d:
            o.install_num = d['install_num']
        return o


