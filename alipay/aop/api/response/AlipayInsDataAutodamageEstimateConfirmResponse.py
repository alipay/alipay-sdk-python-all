#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsDataAutodamageEstimateConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataAutodamageEstimateConfirmResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayInsDataAutodamageEstimateConfirmResponse, self).parse_response_content(response_content)
