#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BsBillDetail import BsBillDetail


class AlipayCommerceOperationBsBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBsBillQueryResponse, self).__init__()
        self._bill_details = None
        self._next_cursor = None
        self._total_count = None

    @property
    def bill_details(self):
        return self._bill_details

    @bill_details.setter
    def bill_details(self, value):
        if isinstance(value, list):
            self._bill_details = list()
            for i in value:
                if isinstance(i, BsBillDetail):
                    self._bill_details.append(i)
                else:
                    self._bill_details.append(BsBillDetail.from_alipay_dict(i))
    @property
    def next_cursor(self):
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self._next_cursor = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBsBillQueryResponse, self).parse_response_content(response_content)
        if 'bill_details' in response:
            self.bill_details = response['bill_details']
        if 'next_cursor' in response:
            self.next_cursor = response['next_cursor']
        if 'total_count' in response:
            self.total_count = response['total_count']
