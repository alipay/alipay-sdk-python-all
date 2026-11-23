#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentGlassesLeaseSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentGlassesLeaseSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentGlassesLeaseSyncResponse, self).parse_response_content(response_content)
