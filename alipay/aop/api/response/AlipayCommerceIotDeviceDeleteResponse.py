#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceDeleteResponse, self).parse_response_content(response_content)
