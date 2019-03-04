#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAppPageUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAppPageUploadResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAppPageUploadResponse, self).parse_response_content(response_content)
