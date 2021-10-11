#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceEcoUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceEcoUnbindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceEcoUnbindResponse, self).parse_response_content(response_content)
