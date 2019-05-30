#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAliyunbenefitReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAliyunbenefitReceiveResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserAliyunbenefitReceiveResponse, self).parse_response_content(response_content)
