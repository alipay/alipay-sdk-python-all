#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePropertyVideocallAnswerNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyVideocallAnswerNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyVideocallAnswerNotifyResponse, self).parse_response_content(response_content)
