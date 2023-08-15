#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DataBillResult import DataBillResult


class AnttechMorseMarketingDataBillBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingDataBillBatchqueryResponse, self).__init__()
        self._bills = None
        self._count = None
        self._out_biz_no = None
        self._page_num = None
        self._page_size = None

    @property
    def bills(self):
        return self._bills

    @bills.setter
    def bills(self, value):
        if isinstance(value, list):
            self._bills = list()
            for i in value:
                if isinstance(i, DataBillResult):
                    self._bills.append(i)
                else:
                    self._bills.append(DataBillResult.from_alipay_dict(i))
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingDataBillBatchqueryResponse, self).parse_response_content(response_content)
        if 'bills' in response:
            self.bills = response['bills']
        if 'count' in response:
            self.count = response['count']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
