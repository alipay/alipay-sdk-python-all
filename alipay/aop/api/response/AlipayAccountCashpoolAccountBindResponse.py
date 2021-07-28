#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountCashpoolAccountBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountCashpoolAccountBindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayAccountCashpoolAccountBindResponse, self).parse_response_content(response_content)
