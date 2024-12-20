#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandDirectAgentCheckResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandDirectAgentCheckResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandDirectAgentCheckResponse, self).parse_response_content(response_content)
