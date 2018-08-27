#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppPdeductSignValidateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppPdeductSignValidateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppPdeductSignValidateResponse, self).parse_response_content(response_content)
