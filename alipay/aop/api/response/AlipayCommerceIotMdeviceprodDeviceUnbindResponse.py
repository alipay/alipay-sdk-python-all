#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMdeviceprodDeviceUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMdeviceprodDeviceUnbindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMdeviceprodDeviceUnbindResponse, self).parse_response_content(response_content)
