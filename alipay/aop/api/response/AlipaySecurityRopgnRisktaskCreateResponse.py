#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRopgnRisktaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRopgnRisktaskCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRopgnRisktaskCreateResponse, self).parse_response_content(response_content)
