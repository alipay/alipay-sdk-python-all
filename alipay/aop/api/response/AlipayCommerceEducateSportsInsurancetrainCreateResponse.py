#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSportsInsurancetrainCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSportsInsurancetrainCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSportsInsurancetrainCreateResponse, self).parse_response_content(response_content)
