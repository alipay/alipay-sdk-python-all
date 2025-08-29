#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCareertrainingOrginfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingOrginfoModifyResponse, self).__init__()
        self._org_code = None

    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingOrginfoModifyResponse, self).parse_response_content(response_content)
        if 'org_code' in response:
            self.org_code = response['org_code']
