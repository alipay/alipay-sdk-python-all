#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupGroupcontrolCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupcontrolCreateormodifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupcontrolCreateormodifyResponse, self).parse_response_content(response_content)
