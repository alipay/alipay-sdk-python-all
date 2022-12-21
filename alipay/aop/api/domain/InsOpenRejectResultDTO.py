#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenRejectResultDTO(object):

    def __init__(self):
        self._product_code = None
        self._product_name = None
        self._reject_reason_code = None
        self._reject_reason_msg = None

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def reject_reason_code(self):
        return self._reject_reason_code

    @reject_reason_code.setter
    def reject_reason_code(self, value):
        self._reject_reason_code = value
    @property
    def reject_reason_msg(self):
        return self._reject_reason_msg

    @reject_reason_msg.setter
    def reject_reason_msg(self, value):
        self._reject_reason_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.reject_reason_code:
            if hasattr(self.reject_reason_code, 'to_alipay_dict'):
                params['reject_reason_code'] = self.reject_reason_code.to_alipay_dict()
            else:
                params['reject_reason_code'] = self.reject_reason_code
        if self.reject_reason_msg:
            if hasattr(self.reject_reason_msg, 'to_alipay_dict'):
                params['reject_reason_msg'] = self.reject_reason_msg.to_alipay_dict()
            else:
                params['reject_reason_msg'] = self.reject_reason_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenRejectResultDTO()
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'reject_reason_code' in d:
            o.reject_reason_code = d['reject_reason_code']
        if 'reject_reason_msg' in d:
            o.reject_reason_msg = d['reject_reason_msg']
        return o


