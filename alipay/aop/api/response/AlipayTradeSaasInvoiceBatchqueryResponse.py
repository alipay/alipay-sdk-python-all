#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceDetailInfo import InvoiceDetailInfo


class AlipayTradeSaasInvoiceBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasInvoiceBatchqueryResponse, self).__init__()
        self._has_next = None
        self._invoice_detail_info_list = None
        self._page_no = None
        self._page_size = None
        self._total_count = None

    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def invoice_detail_info_list(self):
        return self._invoice_detail_info_list

    @invoice_detail_info_list.setter
    def invoice_detail_info_list(self, value):
        if isinstance(value, InvoiceDetailInfo):
            self._invoice_detail_info_list = value
        else:
            self._invoice_detail_info_list = InvoiceDetailInfo.from_alipay_dict(value)
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasInvoiceBatchqueryResponse, self).parse_response_content(response_content)
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'invoice_detail_info_list' in response:
            self.invoice_detail_info_list = response['invoice_detail_info_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
