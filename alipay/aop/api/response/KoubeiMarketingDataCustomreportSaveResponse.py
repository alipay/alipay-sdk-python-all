#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataCustomreportSaveResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataCustomreportSaveResponse, self).__init__()
        self._condition_key = None

    @property
    def condition_key(self):
        return self._condition_key

    @condition_key.setter
    def condition_key(self, value):
        self._condition_key = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataCustomreportSaveResponse, self).parse_response_content(response_content)
        if 'condition_key' in response:
            self.condition_key = response['condition_key']
