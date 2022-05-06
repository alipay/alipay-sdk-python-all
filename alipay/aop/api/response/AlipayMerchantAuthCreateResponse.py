#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantAuthCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantAuthCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantAuthCreateResponse, self).parse_response_content(response_content)
