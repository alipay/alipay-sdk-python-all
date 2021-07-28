#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdDataQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdDataQueryResponse, self).parse_response_content(response_content)
