#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserTradeInfoDTO import UserTradeInfoDTO


class AlipayFundUsertradeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundUsertradeBatchqueryResponse, self).__init__()
        self._end_time = None
        self._has_next = None
        self._page_index = None
        self._page_size = None
        self._start_time = None
        self._total_count = None
        self._trade_info_list = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
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
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def trade_info_list(self):
        return self._trade_info_list

    @trade_info_list.setter
    def trade_info_list(self, value):
        if isinstance(value, list):
            self._trade_info_list = list()
            for i in value:
                if isinstance(i, UserTradeInfoDTO):
                    self._trade_info_list.append(i)
                else:
                    self._trade_info_list.append(UserTradeInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundUsertradeBatchqueryResponse, self).parse_response_content(response_content)
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'trade_info_list' in response:
            self.trade_info_list = response['trade_info_list']
