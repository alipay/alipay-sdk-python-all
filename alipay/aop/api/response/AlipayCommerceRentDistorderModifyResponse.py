#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentDistorderModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentDistorderModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentDistorderModifyResponse, self).parse_response_content(response_content)
