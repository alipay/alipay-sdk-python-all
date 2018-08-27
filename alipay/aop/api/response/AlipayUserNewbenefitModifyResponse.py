#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserNewbenefitModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserNewbenefitModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserNewbenefitModifyResponse, self).parse_response_content(response_content)
