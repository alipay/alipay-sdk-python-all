#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportParkingExitinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportParkingExitinfoSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportParkingExitinfoSyncResponse, self).parse_response_content(response_content)
