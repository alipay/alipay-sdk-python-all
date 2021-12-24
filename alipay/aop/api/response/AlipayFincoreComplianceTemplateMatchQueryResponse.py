#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceTemplateMatchQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateMatchQueryResponse, self).__init__()
        self._template_codes = None

    @property
    def template_codes(self):
        return self._template_codes

    @template_codes.setter
    def template_codes(self, value):
        self._template_codes = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateMatchQueryResponse, self).parse_response_content(response_content)
        if 'template_codes' in response:
            self.template_codes = response['template_codes']
