#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpusCreateResponse import OpusCreateResponse


class KoubeiServindustryPortfolioOpusCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryPortfolioOpusCreateResponse, self).__init__()
        self._opuses = None

    @property
    def opuses(self):
        return self._opuses

    @opuses.setter
    def opuses(self, value):
        if isinstance(value, OpusCreateResponse):
            self._opuses = value
        else:
            self._opuses = OpusCreateResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryPortfolioOpusCreateResponse, self).parse_response_content(response_content)
        if 'opuses' in response:
            self.opuses = response['opuses']
