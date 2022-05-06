#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneMarketingEquitycodeDiscryptGetResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneMarketingEquitycodeDiscryptGetResponse, self).__init__()
        self._equity_code = None
        self._should_retry = None

    @property
    def equity_code(self):
        return self._equity_code

    @equity_code.setter
    def equity_code(self, value):
        self._equity_code = value
    @property
    def should_retry(self):
        return self._should_retry

    @should_retry.setter
    def should_retry(self, value):
        self._should_retry = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneMarketingEquitycodeDiscryptGetResponse, self).parse_response_content(response_content)
        if 'equity_code' in response:
            self.equity_code = response['equity_code']
        if 'should_retry' in response:
            self.should_retry = response['should_retry']
