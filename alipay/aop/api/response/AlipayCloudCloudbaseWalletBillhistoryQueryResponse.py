#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Bill import Bill


class AlipayCloudCloudbaseWalletBillhistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletBillhistoryQueryResponse, self).__init__()
        self._bills = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def bills(self):
        return self._bills

    @bills.setter
    def bills(self, value):
        if isinstance(value, list):
            self._bills = list()
            for i in value:
                if isinstance(i, Bill):
                    self._bills.append(i)
                else:
                    self._bills.append(Bill.from_alipay_dict(i))
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletBillhistoryQueryResponse, self).parse_response_content(response_content)
        if 'bills' in response:
            self.bills = response['bills']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
