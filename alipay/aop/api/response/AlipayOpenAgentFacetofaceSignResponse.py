#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentFacetofaceSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentFacetofaceSignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentFacetofaceSignResponse, self).parse_response_content(response_content)
