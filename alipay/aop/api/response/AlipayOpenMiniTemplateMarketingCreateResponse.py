#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniTemplateMarketingCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTemplateMarketingCreateResponse, self).__init__()
        self._detail_id = None

    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTemplateMarketingCreateResponse, self).parse_response_content(response_content)
        if 'detail_id' in response:
            self.detail_id = response['detail_id']
