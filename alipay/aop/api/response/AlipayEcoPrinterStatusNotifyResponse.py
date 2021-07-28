#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoPrinterStatusNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoPrinterStatusNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoPrinterStatusNotifyResponse, self).parse_response_content(response_content)
