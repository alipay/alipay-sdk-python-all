#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceApccenterAlgorithmbaseinfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceApccenterAlgorithmbaseinfoModifyResponse, self).__init__()
        self._platform_algorithm_code = None
        self._platform_algorithm_source = None

    @property
    def platform_algorithm_code(self):
        return self._platform_algorithm_code

    @platform_algorithm_code.setter
    def platform_algorithm_code(self, value):
        self._platform_algorithm_code = value
    @property
    def platform_algorithm_source(self):
        return self._platform_algorithm_source

    @platform_algorithm_source.setter
    def platform_algorithm_source(self, value):
        self._platform_algorithm_source = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceApccenterAlgorithmbaseinfoModifyResponse, self).parse_response_content(response_content)
        if 'platform_algorithm_code' in response:
            self.platform_algorithm_code = response['platform_algorithm_code']
        if 'platform_algorithm_source' in response:
            self.platform_algorithm_source = response['platform_algorithm_source']
