#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSearchBoxModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchBoxModifyResponse, self).__init__()
        self._module_id = None

    @property
    def module_id(self):
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        self._module_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchBoxModifyResponse, self).parse_response_content(response_content)
        if 'module_id' in response:
            self.module_id = response['module_id']
