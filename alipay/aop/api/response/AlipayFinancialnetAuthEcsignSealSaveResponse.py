#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthEcsignSealSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignSealSaveResponse, self).__init__()
        self._seal_id = None

    @property
    def seal_id(self):
        return self._seal_id

    @seal_id.setter
    def seal_id(self, value):
        self._seal_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignSealSaveResponse, self).parse_response_content(response_content)
        if 'seal_id' in response:
            self.seal_id = response['seal_id']
