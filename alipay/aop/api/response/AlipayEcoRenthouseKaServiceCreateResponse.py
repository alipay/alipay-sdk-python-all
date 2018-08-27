#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoRenthouseKaServiceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoRenthouseKaServiceCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoRenthouseKaServiceCreateResponse, self).parse_response_content(response_content)
