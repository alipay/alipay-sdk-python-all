#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationUserPointExchangeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationUserPointExchangeResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationUserPointExchangeResponse, self).parse_response_content(response_content)
