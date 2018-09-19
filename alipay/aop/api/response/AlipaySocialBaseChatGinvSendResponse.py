#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseChatGinvSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseChatGinvSendResponse, self).__init__()
        self._result_tip = None

    @property
    def result_tip(self):
        return self._result_tip

    @result_tip.setter
    def result_tip(self, value):
        self._result_tip = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseChatGinvSendResponse, self).parse_response_content(response_content)
        if 'result_tip' in response:
            self.result_tip = response['result_tip']
