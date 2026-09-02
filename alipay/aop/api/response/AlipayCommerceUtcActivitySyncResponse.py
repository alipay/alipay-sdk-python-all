#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceUtcActivitySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceUtcActivitySyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceUtcActivitySyncResponse, self).parse_response_content(response_content)
