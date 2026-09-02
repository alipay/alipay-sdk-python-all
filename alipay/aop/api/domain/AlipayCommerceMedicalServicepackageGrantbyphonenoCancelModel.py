#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServicepackageGrantbyphonenoCancelModel(object):

    def __init__(self):
        self._order_no_list = None

    @property
    def order_no_list(self):
        return self._order_no_list

    @order_no_list.setter
    def order_no_list(self, value):
        if isinstance(value, list):
            self._order_no_list = list()
            for i in value:
                self._order_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.order_no_list:
            if isinstance(self.order_no_list, list):
                for i in range(0, len(self.order_no_list)):
                    element = self.order_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_no_list[i] = element.to_alipay_dict()
            if hasattr(self.order_no_list, 'to_alipay_dict'):
                params['order_no_list'] = self.order_no_list.to_alipay_dict()
            else:
                params['order_no_list'] = self.order_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServicepackageGrantbyphonenoCancelModel()
        if 'order_no_list' in d:
            o.order_no_list = d['order_no_list']
        return o


