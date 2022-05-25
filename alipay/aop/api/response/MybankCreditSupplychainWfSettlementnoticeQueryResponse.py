#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainWfSettlementnoticeQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfSettlementnoticeQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfSettlementnoticeQueryResponse, self).parse_response_content(response_content)
