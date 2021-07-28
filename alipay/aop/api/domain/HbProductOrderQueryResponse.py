#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductOrderDTO import ProductOrderDTO


class HbProductOrderQueryResponse(object):

    def __init__(self):
        self._error_code = None
        self._error_message = None
        self._product_order_list = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def product_order_list(self):
        return self._product_order_list

    @product_order_list.setter
    def product_order_list(self, value):
        if isinstance(value, list):
            self._product_order_list = list()
            for i in value:
                if isinstance(i, ProductOrderDTO):
                    self._product_order_list.append(i)
                else:
                    self._product_order_list.append(ProductOrderDTO.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.product_order_list:
            if isinstance(self.product_order_list, list):
                for i in range(0, len(self.product_order_list)):
                    element = self.product_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_order_list[i] = element.to_alipay_dict()
            if hasattr(self.product_order_list, 'to_alipay_dict'):
                params['product_order_list'] = self.product_order_list.to_alipay_dict()
            else:
                params['product_order_list'] = self.product_order_list
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HbProductOrderQueryResponse()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'product_order_list' in d:
            o.product_order_list = d['product_order_list']
        if 'success' in d:
            o.success = d['success']
        return o


