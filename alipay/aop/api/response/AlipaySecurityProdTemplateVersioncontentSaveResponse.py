#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTemplateVersioncontentSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateVersioncontentSaveResponse, self).__init__()
        self._save_result = None

    @property
    def save_result(self):
        return self._save_result

    @save_result.setter
    def save_result(self, value):
        self._save_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateVersioncontentSaveResponse, self).parse_response_content(response_content)
        if 'save_result' in response:
            self.save_result = response['save_result']
