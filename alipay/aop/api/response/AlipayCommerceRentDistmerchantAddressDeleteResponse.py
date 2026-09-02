#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentDistmerchantAddressDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentDistmerchantAddressDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentDistmerchantAddressDeleteResponse, self).parse_response_content(response_content)
