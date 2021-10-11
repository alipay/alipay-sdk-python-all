#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSearchBaseorderModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchBaseorderModifyResponse, self).__init__()
        self._apply_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchBaseorderModifyResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
