#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantLimit(object):

    def __init__(self):
        self._limit_merchant_list = None
        self._limit_type = None

    @property
    def limit_merchant_list(self):
        return self._limit_merchant_list

    @limit_merchant_list.setter
    def limit_merchant_list(self, value):
        if isinstance(value, list):
            self._limit_merchant_list = list()
            for i in value:
                self._limit_merchant_list.append(i)
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit_merchant_list:
            if isinstance(self.limit_merchant_list, list):
                for i in range(0, len(self.limit_merchant_list)):
                    element = self.limit_merchant_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.limit_merchant_list[i] = element.to_alipay_dict()
            if hasattr(self.limit_merchant_list, 'to_alipay_dict'):
                params['limit_merchant_list'] = self.limit_merchant_list.to_alipay_dict()
            else:
                params['limit_merchant_list'] = self.limit_merchant_list
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantLimit()
        if 'limit_merchant_list' in d:
            o.limit_merchant_list = d['limit_merchant_list']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        return o


