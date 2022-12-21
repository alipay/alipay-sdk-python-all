#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSearchAppkeywordDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchAppkeywordDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchAppkeywordDeleteResponse, self).parse_response_content(response_content)
