#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceTaskTradeInfo import InvoiceTaskTradeInfo


class AlipayFundMbpcardInvoicetasktradeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundMbpcardInvoicetasktradeBatchqueryResponse, self).__init__()
        self._current_page = None
        self._has_next = None
        self._invoice_trade_list = None
        self._page_size = None
        self._total_num = None
        self._total_page = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def invoice_trade_list(self):
        return self._invoice_trade_list

    @invoice_trade_list.setter
    def invoice_trade_list(self, value):
        if isinstance(value, list):
            self._invoice_trade_list = list()
            for i in value:
                if isinstance(i, InvoiceTaskTradeInfo):
                    self._invoice_trade_list.append(i)
                else:
                    self._invoice_trade_list.append(InvoiceTaskTradeInfo.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundMbpcardInvoicetasktradeBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'invoice_trade_list' in response:
            self.invoice_trade_list = response['invoice_trade_list']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_page' in response:
            self.total_page = response['total_page']
