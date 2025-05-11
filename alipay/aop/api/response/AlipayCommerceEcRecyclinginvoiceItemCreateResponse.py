#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceItemCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceItemCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceItemCreateResponse, self).parse_response_content(response_content)
