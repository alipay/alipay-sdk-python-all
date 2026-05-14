#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupBuyVerifyDetailList import GroupBuyVerifyDetailList


class AlipayMerchantVerifyHistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantVerifyHistoryQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._total_count = None
        self._verify_list = None

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
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def verify_list(self):
        return self._verify_list

    @verify_list.setter
    def verify_list(self, value):
        if isinstance(value, GroupBuyVerifyDetailList):
            self._verify_list = value
        else:
            self._verify_list = GroupBuyVerifyDetailList.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantVerifyHistoryQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'verify_list' in response:
            self.verify_list = response['verify_list']
