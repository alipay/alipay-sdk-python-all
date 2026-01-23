#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailBenefitpauseSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailBenefitpauseSetResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailBenefitpauseSetResponse, self).parse_response_content(response_content)
