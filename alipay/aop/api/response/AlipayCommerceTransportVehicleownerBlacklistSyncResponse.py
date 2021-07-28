#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportVehicleownerBlacklistSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehicleownerBlacklistSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehicleownerBlacklistSyncResponse, self).parse_response_content(response_content)
