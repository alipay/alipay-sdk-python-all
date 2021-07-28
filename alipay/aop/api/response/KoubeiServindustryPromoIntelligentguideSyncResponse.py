#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvalidTradeDetail import InvalidTradeDetail


class KoubeiServindustryPromoIntelligentguideSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryPromoIntelligentguideSyncResponse, self).__init__()
        self._failure_count = None
        self._invalid_trade_details = None
        self._success_count = None

    @property
    def failure_count(self):
        return self._failure_count

    @failure_count.setter
    def failure_count(self, value):
        self._failure_count = value
    @property
    def invalid_trade_details(self):
        return self._invalid_trade_details

    @invalid_trade_details.setter
    def invalid_trade_details(self, value):
        if isinstance(value, list):
            self._invalid_trade_details = list()
            for i in value:
                if isinstance(i, InvalidTradeDetail):
                    self._invalid_trade_details.append(i)
                else:
                    self._invalid_trade_details.append(InvalidTradeDetail.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryPromoIntelligentguideSyncResponse, self).parse_response_content(response_content)
        if 'failure_count' in response:
            self.failure_count = response['failure_count']
        if 'invalid_trade_details' in response:
            self.invalid_trade_details = response['invalid_trade_details']
        if 'success_count' in response:
            self.success_count = response['success_count']
