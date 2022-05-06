#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCityserviceOpeneventAppModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceOpeneventAppModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceOpeneventAppModifyResponse, self).parse_response_content(response_content)
