#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceSendOpenByAlipayTradeNo import InvoiceSendOpenByAlipayTradeNo


class AlipayEbppInvoiceAlipaytradeSendModel(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._invoice_info_list = None
        self._m_short_name = None
        self._sub_m_short_name = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def invoice_info_list(self):
        return self._invoice_info_list

    @invoice_info_list.setter
    def invoice_info_list(self, value):
        if isinstance(value, list):
            self._invoice_info_list = list()
            for i in value:
                if isinstance(i, InvoiceSendOpenByAlipayTradeNo):
                    self._invoice_info_list.append(i)
                else:
                    self._invoice_info_list.append(InvoiceSendOpenByAlipayTradeNo.from_alipay_dict(i))
    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
    @property
    def sub_m_short_name(self):
        return self._sub_m_short_name

    @sub_m_short_name.setter
    def sub_m_short_name(self, value):
        self._sub_m_short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.invoice_info_list:
            if isinstance(self.invoice_info_list, list):
                for i in range(0, len(self.invoice_info_list)):
                    element = self.invoice_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_info_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_info_list, 'to_alipay_dict'):
                params['invoice_info_list'] = self.invoice_info_list.to_alipay_dict()
            else:
                params['invoice_info_list'] = self.invoice_info_list
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
        if self.sub_m_short_name:
            if hasattr(self.sub_m_short_name, 'to_alipay_dict'):
                params['sub_m_short_name'] = self.sub_m_short_name.to_alipay_dict()
            else:
                params['sub_m_short_name'] = self.sub_m_short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceAlipaytradeSendModel()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'invoice_info_list' in d:
            o.invoice_info_list = d['invoice_info_list']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        return o


