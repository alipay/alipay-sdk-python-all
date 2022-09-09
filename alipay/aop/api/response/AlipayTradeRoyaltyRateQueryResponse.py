#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeRoyaltyRateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRoyaltyRateQueryResponse, self).__init__()
        self._max_ratio = None
        self._user_id = None

    @property
    def max_ratio(self):
        return self._max_ratio

    @max_ratio.setter
    def max_ratio(self, value):
        self._max_ratio = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRoyaltyRateQueryResponse, self).parse_response_content(response_content)
        if 'max_ratio' in response:
            self.max_ratio = response['max_ratio']
        if 'user_id' in response:
            self.user_id = response['user_id']
