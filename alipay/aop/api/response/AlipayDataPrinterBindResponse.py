#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataPrinterBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataPrinterBindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDataPrinterBindResponse, self).parse_response_content(response_content)
