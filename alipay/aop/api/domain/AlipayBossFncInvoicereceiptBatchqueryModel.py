#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncInvoicereceiptBatchqueryModel(object):

    def __init__(self):
        self._bill_nos = None
        self._out_biz_type = None

    @property
    def bill_nos(self):
        return self._bill_nos

    @bill_nos.setter
    def bill_nos(self, value):
        if isinstance(value, list):
            self._bill_nos = list()
            for i in value:
                self._bill_nos.append(i)
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_nos:
            if isinstance(self.bill_nos, list):
                for i in range(0, len(self.bill_nos)):
                    element = self.bill_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_nos[i] = element.to_alipay_dict()
            if hasattr(self.bill_nos, 'to_alipay_dict'):
                params['bill_nos'] = self.bill_nos.to_alipay_dict()
            else:
                params['bill_nos'] = self.bill_nos
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoicereceiptBatchqueryModel()
        if 'bill_nos' in d:
            o.bill_nos = d['bill_nos']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        return o


