#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HonorLoanRecordDTO import HonorLoanRecordDTO


class AlipayPcreditLoanHonorLoanBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorLoanBatchqueryResponse, self).__init__()
        self._current_page = None
        self._page_size = None
        self._records = None
        self._total_count = None
        self._total_num = None
        self._total_page = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, HonorLoanRecordDTO):
                    self._records.append(i)
                else:
                    self._records.append(HonorLoanRecordDTO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
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
        response = super(AlipayPcreditLoanHonorLoanBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'records' in response:
            self.records = response['records']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_page' in response:
            self.total_page = response['total_page']
