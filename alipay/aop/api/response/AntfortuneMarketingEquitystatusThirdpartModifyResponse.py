#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneMarketingEquitystatusThirdpartModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneMarketingEquitystatusThirdpartModifyResponse, self).__init__()
        self._should_retry = None

    @property
    def should_retry(self):
        return self._should_retry

    @should_retry.setter
    def should_retry(self, value):
        self._should_retry = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneMarketingEquitystatusThirdpartModifyResponse, self).parse_response_content(response_content)
        if 'should_retry' in response:
            self.should_retry = response['should_retry']
