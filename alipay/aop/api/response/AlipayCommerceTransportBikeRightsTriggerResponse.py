#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportBikeRightsTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportBikeRightsTriggerResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportBikeRightsTriggerResponse, self).parse_response_content(response_content)
