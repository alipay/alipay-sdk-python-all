#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantQipanCrowdwithturingtagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanCrowdwithturingtagQueryResponse, self).__init__()
        self._count_range = None

    @property
    def count_range(self):
        return self._count_range

    @count_range.setter
    def count_range(self, value):
        self._count_range = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanCrowdwithturingtagQueryResponse, self).parse_response_content(response_content)
        if 'count_range' in response:
            self.count_range = response['count_range']
