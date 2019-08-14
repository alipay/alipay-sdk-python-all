#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TrusteeshipAccountBillQueryResponse import TrusteeshipAccountBillQueryResponse


class AlipayFundAccountBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountBillQueryResponse, self).__init__()
        self._acc_detail_list = None
        self._page_num = None
        self._page_size = None
        self._total_item_count = None

    @property
    def acc_detail_list(self):
        return self._acc_detail_list

    @acc_detail_list.setter
    def acc_detail_list(self, value):
        if isinstance(value, list):
            self._acc_detail_list = list()
            for i in value:
                if isinstance(i, TrusteeshipAccountBillQueryResponse):
                    self._acc_detail_list.append(i)
                else:
                    self._acc_detail_list.append(TrusteeshipAccountBillQueryResponse.from_alipay_dict(i))
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
    def total_item_count(self):
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, value):
        self._total_item_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountBillQueryResponse, self).parse_response_content(response_content)
        if 'acc_detail_list' in response:
            self.acc_detail_list = response['acc_detail_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_item_count' in response:
            self.total_item_count = response['total_item_count']
