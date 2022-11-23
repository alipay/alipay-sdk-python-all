#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityDumQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDumQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDumQueryResponse, self).parse_response_content(response_content)
