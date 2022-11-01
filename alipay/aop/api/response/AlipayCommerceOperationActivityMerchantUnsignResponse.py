#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationActivityMerchantUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationActivityMerchantUnsignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationActivityMerchantUnsignResponse, self).parse_response_content(response_content)
