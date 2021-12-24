#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SummaryInvoiceBillOpenDTO import SummaryInvoiceBillOpenDTO


class AlipayEbppInvoiceEnterpriseSummaryinvoicebillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseSummaryinvoicebillQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._summary_invoice_bill_list = None
        self._total_size = None

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
    def summary_invoice_bill_list(self):
        return self._summary_invoice_bill_list

    @summary_invoice_bill_list.setter
    def summary_invoice_bill_list(self, value):
        if isinstance(value, list):
            self._summary_invoice_bill_list = list()
            for i in value:
                if isinstance(i, SummaryInvoiceBillOpenDTO):
                    self._summary_invoice_bill_list.append(i)
                else:
                    self._summary_invoice_bill_list.append(SummaryInvoiceBillOpenDTO.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseSummaryinvoicebillQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'summary_invoice_bill_list' in response:
            self.summary_invoice_bill_list = response['summary_invoice_bill_list']
        if 'total_size' in response:
            self.total_size = response['total_size']
