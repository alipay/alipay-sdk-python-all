#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentSubmerchantCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentSubmerchantCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentSubmerchantCreateResponse, self).parse_response_content(response_content)
