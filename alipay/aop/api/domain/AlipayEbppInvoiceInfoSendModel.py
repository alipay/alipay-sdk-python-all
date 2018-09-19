#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceSendOpenModel import InvoiceSendOpenModel


class AlipayEbppInvoiceInfoSendModel(object):

    def __init__(self):
        self._invoice_info_list = None
        self._m_short_name = None
        self._sub_m_short_name = None

    @property
    def invoice_info_list(self):
        return self._invoice_info_list

    @invoice_info_list.setter
    def invoice_info_list(self, value):
        if isinstance(value, list):
            self._invoice_info_list = list()
            for i in value:
                if isinstance(i, InvoiceSendOpenModel):
                    self._invoice_info_list.append(i)
                else:
                    self._invoice_info_list.append(InvoiceSendOpenModel.from_alipay_dict(i))
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
        o = AlipayEbppInvoiceInfoSendModel()
        if 'invoice_info_list' in d:
            o.invoice_info_list = d['invoice_info_list']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        return o


