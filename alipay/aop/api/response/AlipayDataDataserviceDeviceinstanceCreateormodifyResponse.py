#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceDeviceinstanceCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceDeviceinstanceCreateormodifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceDeviceinstanceCreateormodifyResponse, self).parse_response_content(response_content)
