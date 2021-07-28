#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingIotMerchantplanCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingIotMerchantplanCancelResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMarketingIotMerchantplanCancelResponse, self).parse_response_content(response_content)
