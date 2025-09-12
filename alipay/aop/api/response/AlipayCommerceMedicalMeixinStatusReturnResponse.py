#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMeixinStatusReturnResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMeixinStatusReturnResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMeixinStatusReturnResponse, self).parse_response_content(response_content)
