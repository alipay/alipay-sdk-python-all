#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradeItemResult import TradeItemResult


class AlipayDataBillSellQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataBillSellQueryResponse, self).__init__()
        self._detail_list = None
        self._page_no = None
        self._page_size = None
        self._total_size = None

    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, TradeItemResult):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(TradeItemResult.from_alipay_dict(i))
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
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataBillSellQueryResponse, self).parse_response_content(response_content)
        if 'detail_list' in response:
            self.detail_list = response['detail_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
