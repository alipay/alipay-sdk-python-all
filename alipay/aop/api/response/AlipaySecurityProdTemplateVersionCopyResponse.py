#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTemplateVersionCopyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateVersionCopyResponse, self).__init__()
        self._copy_result = None
        self._version_no = None

    @property
    def copy_result(self):
        return self._copy_result

    @copy_result.setter
    def copy_result(self, value):
        self._copy_result = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateVersionCopyResponse, self).parse_response_content(response_content)
        if 'copy_result' in response:
            self.copy_result = response['copy_result']
        if 'version_no' in response:
            self.version_no = response['version_no']
