#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayOrderDataOpenapiResultInfo import AlipayOrderDataOpenapiResultInfo


class AlipayMerchantOrderDigestUnlimitedBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantOrderDigestUnlimitedBatchqueryResponse, self).__init__()
        self._has_next_page = None
        self._order_list = None

    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, AlipayOrderDataOpenapiResultInfo):
                    self._order_list.append(i)
                else:
                    self._order_list.append(AlipayOrderDataOpenapiResultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantOrderDigestUnlimitedBatchqueryResponse, self).parse_response_content(response_content)
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'order_list' in response:
            self.order_list = response['order_list']
