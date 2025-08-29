#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentRoyaltyInvestApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentRoyaltyInvestApplyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentRoyaltyInvestApplyResponse, self).parse_response_content(response_content)
