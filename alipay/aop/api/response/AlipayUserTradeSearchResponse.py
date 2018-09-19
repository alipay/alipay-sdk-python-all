#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradeRecord import TradeRecord


class AlipayUserTradeSearchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserTradeSearchResponse, self).__init__()
        self._total_pages = None
        self._total_results = None
        self._trade_records = None

    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_results(self):
        return self._total_results

    @total_results.setter
    def total_results(self, value):
        self._total_results = value
    @property
    def trade_records(self):
        return self._trade_records

    @trade_records.setter
    def trade_records(self, value):
        if isinstance(value, list):
            self._trade_records = list()
            for i in value:
                if isinstance(i, TradeRecord):
                    self._trade_records.append(i)
                else:
                    self._trade_records.append(TradeRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserTradeSearchResponse, self).parse_response_content(response_content)
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_results' in response:
            self.total_results = response['total_results']
        if 'trade_records' in response:
            self.trade_records = response['trade_records']
