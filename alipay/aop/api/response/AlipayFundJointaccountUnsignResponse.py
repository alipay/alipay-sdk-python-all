#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountUnsignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountUnsignResponse, self).parse_response_content(response_content)
