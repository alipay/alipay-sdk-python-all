#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceInputparamcheckRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceInputparamcheckRainystestQueryResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceInputparamcheckRainystestQueryResponse, self).parse_response_content(response_content)
