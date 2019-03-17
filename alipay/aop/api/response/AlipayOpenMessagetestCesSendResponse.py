#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMessagetestCesSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMessagetestCesSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMessagetestCesSendResponse, self).parse_response_content(response_content)
