#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayDeviceNlinkMerchantSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayDeviceNlinkMerchantSubmitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayPayDeviceNlinkMerchantSubmitResponse, self).parse_response_content(response_content)
