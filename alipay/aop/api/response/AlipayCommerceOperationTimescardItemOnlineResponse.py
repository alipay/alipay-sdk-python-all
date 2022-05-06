#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationTimescardItemOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTimescardItemOnlineResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTimescardItemOnlineResponse, self).parse_response_content(response_content)
