#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCrowdMatchedQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCrowdMatchedQueryResponse, self).__init__()
        self._matched_res = None

    @property
    def matched_res(self):
        return self._matched_res

    @matched_res.setter
    def matched_res(self, value):
        self._matched_res = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCrowdMatchedQueryResponse, self).parse_response_content(response_content)
        if 'matched_res' in response:
            self.matched_res = response['matched_res']
