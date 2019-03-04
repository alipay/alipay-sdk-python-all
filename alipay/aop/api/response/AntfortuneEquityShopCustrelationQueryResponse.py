#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneEquityShopCustrelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneEquityShopCustrelationQueryResponse, self).__init__()
        self._follow_time = None
        self._match_result = None

    @property
    def follow_time(self):
        return self._follow_time

    @follow_time.setter
    def follow_time(self, value):
        self._follow_time = value
    @property
    def match_result(self):
        return self._match_result

    @match_result.setter
    def match_result(self, value):
        self._match_result = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneEquityShopCustrelationQueryResponse, self).parse_response_content(response_content)
        if 'follow_time' in response:
            self.follow_time = response['follow_time']
        if 'match_result' in response:
            self.match_result = response['match_result']
