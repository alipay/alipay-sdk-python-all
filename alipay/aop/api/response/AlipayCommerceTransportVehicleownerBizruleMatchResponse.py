#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportVehicleownerBizruleMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehicleownerBizruleMatchResponse, self).__init__()
        self._match_result = None

    @property
    def match_result(self):
        return self._match_result

    @match_result.setter
    def match_result(self, value):
        self._match_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehicleownerBizruleMatchResponse, self).parse_response_content(response_content)
        if 'match_result' in response:
            self.match_result = response['match_result']
