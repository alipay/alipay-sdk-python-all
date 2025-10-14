#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EbikeBindServiceStatisticsDTO import EbikeBindServiceStatisticsDTO


class AlipayCommerceTransportIndustryEbikestatisticsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIndustryEbikestatisticsQueryResponse, self).__init__()
        self._date_str = None
        self._page_num = None
        self._page_size = None
        self._query_type = None
        self._record_list = None
        self._total = None

    @property
    def date_str(self):
        return self._date_str

    @date_str.setter
    def date_str(self, value):
        self._date_str = value
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
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, EbikeBindServiceStatisticsDTO):
                    self._record_list.append(i)
                else:
                    self._record_list.append(EbikeBindServiceStatisticsDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIndustryEbikestatisticsQueryResponse, self).parse_response_content(response_content)
        if 'date_str' in response:
            self.date_str = response['date_str']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'query_type' in response:
            self.query_type = response['query_type']
        if 'record_list' in response:
            self.record_list = response['record_list']
        if 'total' in response:
            self.total = response['total']
