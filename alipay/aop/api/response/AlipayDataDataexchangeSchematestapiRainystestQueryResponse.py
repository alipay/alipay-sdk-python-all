#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataexchangeSchematestapiRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeSchematestapiRainystestQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeSchematestapiRainystestQueryResponse, self).parse_response_content(response_content)
