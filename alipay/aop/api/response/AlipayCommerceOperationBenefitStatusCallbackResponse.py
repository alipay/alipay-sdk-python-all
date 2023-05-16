#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationBenefitStatusCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBenefitStatusCallbackResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBenefitStatusCallbackResponse, self).parse_response_content(response_content)
