#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationCreditphoneRoutehubCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphoneRoutehubCallbackResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphoneRoutehubCallbackResponse, self).parse_response_content(response_content)
