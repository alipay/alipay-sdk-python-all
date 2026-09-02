#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceBatchdepositApplyModel(object):

    def __init__(self):
        self._order_id_list = None
        self._tax_no = None

    @property
    def order_id_list(self):
        return self._order_id_list

    @order_id_list.setter
    def order_id_list(self, value):
        if isinstance(value, list):
            self._order_id_list = list()
            for i in value:
                self._order_id_list.append(i)
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id_list:
            if isinstance(self.order_id_list, list):
                for i in range(0, len(self.order_id_list)):
                    element = self.order_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_id_list[i] = element.to_alipay_dict()
            if hasattr(self.order_id_list, 'to_alipay_dict'):
                params['order_id_list'] = self.order_id_list.to_alipay_dict()
            else:
                params['order_id_list'] = self.order_id_list
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceBatchdepositApplyModel()
        if 'order_id_list' in d:
            o.order_id_list = d['order_id_list']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


