#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportOnlinerideOrderFreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOnlinerideOrderFreezeResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOnlinerideOrderFreezeResponse, self).parse_response_content(response_content)
