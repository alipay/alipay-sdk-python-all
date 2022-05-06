#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotvspUserDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspUserDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspUserDeleteResponse, self).parse_response_content(response_content)
