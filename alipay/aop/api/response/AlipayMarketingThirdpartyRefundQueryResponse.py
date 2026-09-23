#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ThirdPartyRefundExceptionOrderList import ThirdPartyRefundExceptionOrderList


class AlipayMarketingThirdpartyRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingThirdpartyRefundQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._query_result_list = None
        self._total_count = None

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
    def query_result_list(self):
        return self._query_result_list

    @query_result_list.setter
    def query_result_list(self, value):
        if isinstance(value, ThirdPartyRefundExceptionOrderList):
            self._query_result_list = value
        else:
            self._query_result_list = ThirdPartyRefundExceptionOrderList.from_alipay_dict(value)
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingThirdpartyRefundQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'query_result_list' in response:
            self.query_result_list = response['query_result_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
