#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGamecenterMetricSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGamecenterMetricSubmitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserGamecenterMetricSubmitResponse, self).parse_response_content(response_content)
