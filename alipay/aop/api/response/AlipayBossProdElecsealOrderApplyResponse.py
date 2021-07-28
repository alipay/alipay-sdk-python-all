#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdElecsealOrderApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdElecsealOrderApplyResponse, self).__init__()
        self._seal_request_id = None

    @property
    def seal_request_id(self):
        return self._seal_request_id

    @seal_request_id.setter
    def seal_request_id(self, value):
        self._seal_request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdElecsealOrderApplyResponse, self).parse_response_content(response_content)
        if 'seal_request_id' in response:
            self.seal_request_id = response['seal_request_id']
