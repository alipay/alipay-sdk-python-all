#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementAgentUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementAgentUnsignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementAgentUnsignResponse, self).parse_response_content(response_content)
