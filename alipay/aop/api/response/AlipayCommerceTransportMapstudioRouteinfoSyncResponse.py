#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportMapstudioRouteinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportMapstudioRouteinfoSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportMapstudioRouteinfoSyncResponse, self).parse_response_content(response_content)
