#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateManagerInfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateManagerInfoModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateManagerInfoModifyResponse, self).parse_response_content(response_content)
