#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCouponWufuCardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuCardQueryResponse, self).__init__()
        self._count = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuCardQueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
