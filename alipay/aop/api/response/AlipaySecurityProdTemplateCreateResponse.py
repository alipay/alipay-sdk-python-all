#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateCreateResponse, self).__init__()
        self._template_code = None
        self._version_no = None

    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateCreateResponse, self).parse_response_content(response_content)
        if 'template_code' in response:
            self.template_code = response['template_code']
        if 'version_no' in response:
            self.version_no = response['version_no']
