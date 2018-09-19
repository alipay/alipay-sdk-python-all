#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceModelContent import InvoiceModelContent


class AlipayEbppInvoiceSycnModel(object):

    def __init__(self):
        self._invoice_info = None
        self._m_short_name = None
        self._sub_m_short_name = None

    @property
    def invoice_info(self):
        return self._invoice_info

    @invoice_info.setter
    def invoice_info(self, value):
        if isinstance(value, list):
            self._invoice_info = list()
            for i in value:
                if isinstance(i, InvoiceModelContent):
                    self._invoice_info.append(i)
                else:
                    self._invoice_info.append(InvoiceModelContent.from_alipay_dict(i))
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
        if self.invoice_info:
            if isinstance(self.invoice_info, list):
                for i in range(0, len(self.invoice_info)):
                    element = self.invoice_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_info[i] = element.to_alipay_dict()
            if hasattr(self.invoice_info, 'to_alipay_dict'):
                params['invoice_info'] = self.invoice_info.to_alipay_dict()
            else:
                params['invoice_info'] = self.invoice_info
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
        o = AlipayEbppInvoiceSycnModel()
        if 'invoice_info' in d:
            o.invoice_info = d['invoice_info']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        return o


