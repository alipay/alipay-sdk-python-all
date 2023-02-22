#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingQipanCrowdwithtagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingQipanCrowdwithtagQueryResponse, self).__init__()
        self._count = None
        self._count_range = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def count_range(self):
        return self._count_range

    @count_range.setter
    def count_range(self, value):
        self._count_range = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingQipanCrowdwithtagQueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'count_range' in response:
            self.count_range = response['count_range']
