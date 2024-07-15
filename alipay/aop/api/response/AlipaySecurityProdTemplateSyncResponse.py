#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTemplateSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateSyncResponse, self).__init__()
        self._tgt_template_code = None

    @property
    def tgt_template_code(self):
        return self._tgt_template_code

    @tgt_template_code.setter
    def tgt_template_code(self, value):
        self._tgt_template_code = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateSyncResponse, self).parse_response_content(response_content)
        if 'tgt_template_code' in response:
            self.tgt_template_code = response['tgt_template_code']
