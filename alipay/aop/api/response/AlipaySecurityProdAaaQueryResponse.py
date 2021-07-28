#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdAaaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdAaaQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdAaaQueryResponse, self).parse_response_content(response_content)
