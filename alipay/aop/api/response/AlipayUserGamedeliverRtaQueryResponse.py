#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGamedeliverRtaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGamedeliverRtaQueryResponse, self).__init__()
        self._bid_decision = None

    @property
    def bid_decision(self):
        return self._bid_decision

    @bid_decision.setter
    def bid_decision(self, value):
        self._bid_decision = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGamedeliverRtaQueryResponse, self).parse_response_content(response_content)
        if 'bid_decision' in response:
            self.bid_decision = response['bid_decision']
