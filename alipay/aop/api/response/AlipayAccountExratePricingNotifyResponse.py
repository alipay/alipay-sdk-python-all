#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountExratePricingNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountExratePricingNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayAccountExratePricingNotifyResponse, self).parse_response_content(response_content)
