#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityDataIprVideoCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataIprVideoCallbackResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataIprVideoCallbackResponse, self).parse_response_content(response_content)
