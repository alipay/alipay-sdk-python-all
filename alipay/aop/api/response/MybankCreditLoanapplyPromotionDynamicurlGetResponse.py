#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyPromotionDynamicurlGetResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyPromotionDynamicurlGetResponse, self).__init__()
        self._dynamic_url = None

    @property
    def dynamic_url(self):
        return self._dynamic_url

    @dynamic_url.setter
    def dynamic_url(self, value):
        self._dynamic_url = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyPromotionDynamicurlGetResponse, self).parse_response_content(response_content)
        if 'dynamic_url' in response:
            self.dynamic_url = response['dynamic_url']
