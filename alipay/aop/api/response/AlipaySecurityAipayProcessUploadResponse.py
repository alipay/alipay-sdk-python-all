#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityAipayProcessUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityAipayProcessUploadResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySecurityAipayProcessUploadResponse, self).parse_response_content(response_content)
