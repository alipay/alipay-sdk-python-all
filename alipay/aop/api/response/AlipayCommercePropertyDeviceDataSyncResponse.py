#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePropertyDeviceDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyDeviceDataSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyDeviceDataSyncResponse, self).parse_response_content(response_content)
