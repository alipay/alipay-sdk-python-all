#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountTradePayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountTradePayResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountTradePayResponse, self).parse_response_content(response_content)
