#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceTitle import InvoiceTitle


class AlipayCloudCloudbaseInvoiceGetModel(object):

    def __init__(self):
        self._invoice_title = None
        self._order_no_list = None

    @property
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        if isinstance(value, InvoiceTitle):
            self._invoice_title = value
        else:
            self._invoice_title = InvoiceTitle.from_alipay_dict(value)
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
        if self.invoice_title:
            if hasattr(self.invoice_title, 'to_alipay_dict'):
                params['invoice_title'] = self.invoice_title.to_alipay_dict()
            else:
                params['invoice_title'] = self.invoice_title
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
        o = AlipayCloudCloudbaseInvoiceGetModel()
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'order_no_list' in d:
            o.order_no_list = d['order_no_list']
        return o


