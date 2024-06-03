#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditBusinessPlanCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditBusinessPlanCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(ZhimaCreditBusinessPlanCreateResponse, self).parse_response_content(response_content)
