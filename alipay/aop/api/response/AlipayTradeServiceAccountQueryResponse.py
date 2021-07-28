#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LargeInfiniteCardInfo import LargeInfiniteCardInfo


class AlipayTradeServiceAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeServiceAccountQueryResponse, self).__init__()
        self._large_infinite_card_info = None

    @property
    def large_infinite_card_info(self):
        return self._large_infinite_card_info

    @large_infinite_card_info.setter
    def large_infinite_card_info(self, value):
        if isinstance(value, LargeInfiniteCardInfo):
            self._large_infinite_card_info = value
        else:
            self._large_infinite_card_info = LargeInfiniteCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTradeServiceAccountQueryResponse, self).parse_response_content(response_content)
        if 'large_infinite_card_info' in response:
            self.large_infinite_card_info = response['large_infinite_card_info']
