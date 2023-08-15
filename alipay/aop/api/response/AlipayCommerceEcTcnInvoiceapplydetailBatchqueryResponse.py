#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceApplyDetail import InvoiceApplyDetail


class AlipayCommerceEcTcnInvoiceapplydetailBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTcnInvoiceapplydetailBatchqueryResponse, self).__init__()
        self._detail_list = None
        self._page_num = None
        self._page_size = None
        self._total_size = None

    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, InvoiceApplyDetail):
            self._detail_list = value
        else:
            self._detail_list = InvoiceApplyDetail.from_alipay_dict(value)
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
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTcnInvoiceapplydetailBatchqueryResponse, self).parse_response_content(response_content)
        if 'detail_list' in response:
            self.detail_list = response['detail_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
