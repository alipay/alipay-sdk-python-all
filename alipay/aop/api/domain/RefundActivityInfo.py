#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundActivityInfo(object):

    def __init__(self):
        self._activity_id = None
        self._quantity = None
        self._voucher_code_list = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def voucher_code_list(self):
        return self._voucher_code_list

    @voucher_code_list.setter
    def voucher_code_list(self, value):
        if isinstance(value, list):
            self._voucher_code_list = list()
            for i in value:
                self._voucher_code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.voucher_code_list:
            if isinstance(self.voucher_code_list, list):
                for i in range(0, len(self.voucher_code_list)):
                    element = self.voucher_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_code_list[i] = element.to_alipay_dict()
            if hasattr(self.voucher_code_list, 'to_alipay_dict'):
                params['voucher_code_list'] = self.voucher_code_list.to_alipay_dict()
            else:
                params['voucher_code_list'] = self.voucher_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundActivityInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'voucher_code_list' in d:
            o.voucher_code_list = d['voucher_code_list']
        return o


