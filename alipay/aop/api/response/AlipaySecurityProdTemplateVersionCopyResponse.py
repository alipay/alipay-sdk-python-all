#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTemplateVersionCopyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateVersionCopyResponse, self).__init__()
        self._copy_result = None

    @property
    def copy_result(self):
        return self._copy_result

    @copy_result.setter
    def copy_result(self, value):
        self._copy_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateVersionCopyResponse, self).parse_response_content(response_content)
        if 'copy_result' in response:
            self.copy_result = response['copy_result']
