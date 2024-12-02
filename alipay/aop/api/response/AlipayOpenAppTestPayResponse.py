#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestPayResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestPayResponse, self).parse_response_content(response_content)
