#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppBainaPrizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppBainaPrizeQueryResponse, self).__init__()
        self._eligible_count = None

    @property
    def eligible_count(self):
        return self._eligible_count

    @eligible_count.setter
    def eligible_count(self, value):
        self._eligible_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppBainaPrizeQueryResponse, self).parse_response_content(response_content)
        if 'eligible_count' in response:
            self.eligible_count = response['eligible_count']
