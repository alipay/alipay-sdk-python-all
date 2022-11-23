#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceDeviceinstanceOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceDeviceinstanceOnlineResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceDeviceinstanceOnlineResponse, self).parse_response_content(response_content)
