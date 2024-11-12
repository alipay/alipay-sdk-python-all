#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceOnlineerrorRainyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceOnlineerrorRainyQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceOnlineerrorRainyQueryResponse, self).parse_response_content(response_content)
