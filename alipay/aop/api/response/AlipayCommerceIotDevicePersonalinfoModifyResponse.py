#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDevicePersonalinfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDevicePersonalinfoModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDevicePersonalinfoModifyResponse, self).parse_response_content(response_content)
