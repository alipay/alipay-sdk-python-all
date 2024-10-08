#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupActivityModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupActivityModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupActivityModifyResponse, self).parse_response_content(response_content)
