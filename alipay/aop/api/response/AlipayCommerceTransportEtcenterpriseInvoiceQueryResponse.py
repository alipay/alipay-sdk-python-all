#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EtcCorpInvoiceTrade import EtcCorpInvoiceTrade


class AlipayCommerceTransportEtcenterpriseInvoiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseInvoiceQueryResponse, self).__init__()
        self._has_next = None
        self._invoice_waybill = None
        self._page_num = None
        self._page_size = None
        self._total_page = None
        self._total_size = None

    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def invoice_waybill(self):
        return self._invoice_waybill

    @invoice_waybill.setter
    def invoice_waybill(self, value):
        if isinstance(value, list):
            self._invoice_waybill = list()
            for i in value:
                if isinstance(i, EtcCorpInvoiceTrade):
                    self._invoice_waybill.append(i)
                else:
                    self._invoice_waybill.append(EtcCorpInvoiceTrade.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseInvoiceQueryResponse, self).parse_response_content(response_content)
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'invoice_waybill' in response:
            self.invoice_waybill = response['invoice_waybill']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'total_size' in response:
            self.total_size = response['total_size']
