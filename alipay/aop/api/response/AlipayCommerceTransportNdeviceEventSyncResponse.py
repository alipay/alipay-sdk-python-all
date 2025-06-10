#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportNdeviceEventSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportNdeviceEventSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportNdeviceEventSyncResponse, self).parse_response_content(response_content)
