#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceTaxnoBatchqueryModel(object):

    def __init__(self):
        self._enable_trade_out = None
        self._end_invoice_date = None
        self._invoice_kind_list = None
        self._limit_size = None
        self._page_num = None
        self._scene = None
        self._start_invoice_date = None
        self._tax_no = None

    @property
    def enable_trade_out(self):
        return self._enable_trade_out

    @enable_trade_out.setter
    def enable_trade_out(self, value):
        self._enable_trade_out = value
    @property
    def end_invoice_date(self):
        return self._end_invoice_date

    @end_invoice_date.setter
    def end_invoice_date(self, value):
        self._end_invoice_date = value
    @property
    def invoice_kind_list(self):
        return self._invoice_kind_list

    @invoice_kind_list.setter
    def invoice_kind_list(self, value):
        if isinstance(value, list):
            self._invoice_kind_list = list()
            for i in value:
                self._invoice_kind_list.append(i)
    @property
    def limit_size(self):
        return self._limit_size

    @limit_size.setter
    def limit_size(self, value):
        self._limit_size = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def start_invoice_date(self):
        return self._start_invoice_date

    @start_invoice_date.setter
    def start_invoice_date(self, value):
        self._start_invoice_date = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable_trade_out:
            if hasattr(self.enable_trade_out, 'to_alipay_dict'):
                params['enable_trade_out'] = self.enable_trade_out.to_alipay_dict()
            else:
                params['enable_trade_out'] = self.enable_trade_out
        if self.end_invoice_date:
            if hasattr(self.end_invoice_date, 'to_alipay_dict'):
                params['end_invoice_date'] = self.end_invoice_date.to_alipay_dict()
            else:
                params['end_invoice_date'] = self.end_invoice_date
        if self.invoice_kind_list:
            if isinstance(self.invoice_kind_list, list):
                for i in range(0, len(self.invoice_kind_list)):
                    element = self.invoice_kind_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_kind_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_kind_list, 'to_alipay_dict'):
                params['invoice_kind_list'] = self.invoice_kind_list.to_alipay_dict()
            else:
                params['invoice_kind_list'] = self.invoice_kind_list
        if self.limit_size:
            if hasattr(self.limit_size, 'to_alipay_dict'):
                params['limit_size'] = self.limit_size.to_alipay_dict()
            else:
                params['limit_size'] = self.limit_size
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.start_invoice_date:
            if hasattr(self.start_invoice_date, 'to_alipay_dict'):
                params['start_invoice_date'] = self.start_invoice_date.to_alipay_dict()
            else:
                params['start_invoice_date'] = self.start_invoice_date
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
        o = AlipayEbppInvoiceTaxnoBatchqueryModel()
        if 'enable_trade_out' in d:
            o.enable_trade_out = d['enable_trade_out']
        if 'end_invoice_date' in d:
            o.end_invoice_date = d['end_invoice_date']
        if 'invoice_kind_list' in d:
            o.invoice_kind_list = d['invoice_kind_list']
        if 'limit_size' in d:
            o.limit_size = d['limit_size']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'scene' in d:
            o.scene = d['scene']
        if 'start_invoice_date' in d:
            o.start_invoice_date = d['start_invoice_date']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


