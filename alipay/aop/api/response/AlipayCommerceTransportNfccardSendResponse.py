#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportNfccardSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportNfccardSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportNfccardSendResponse, self).parse_response_content(response_content)
