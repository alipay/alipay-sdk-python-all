#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayDeviceNlinkNfccallbackSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayDeviceNlinkNfccallbackSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayPayDeviceNlinkNfccallbackSyncResponse, self).parse_response_content(response_content)
