#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityJhjtestaaTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityJhjtestaaTestQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySecurityJhjtestaaTestQueryResponse, self).parse_response_content(response_content)
