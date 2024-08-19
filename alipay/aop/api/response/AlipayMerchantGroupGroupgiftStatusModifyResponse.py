#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupGroupgiftStatusModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupgiftStatusModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupgiftStatusModifyResponse, self).parse_response_content(response_content)
