#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BillResult import BillResult


class AnttechMorseMarketingBillsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingBillsBatchqueryResponse, self).__init__()
        self._bills = None
        self._biz_no = None
        self._count = None
        self._page_num = None

    @property
    def bills(self):
        return self._bills

    @bills.setter
    def bills(self, value):
        if isinstance(value, list):
            self._bills = list()
            for i in value:
                if isinstance(i, BillResult):
                    self._bills.append(i)
                else:
                    self._bills.append(BillResult.from_alipay_dict(i))
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingBillsBatchqueryResponse, self).parse_response_content(response_content)
        if 'bills' in response:
            self.bills = response['bills']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'count' in response:
            self.count = response['count']
        if 'page_num' in response:
            self.page_num = response['page_num']
