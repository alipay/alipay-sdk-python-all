#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationUnofficialMaterialSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationUnofficialMaterialSubmitResponse, self).__init__()
        self._response_id = None

    @property
    def response_id(self):
        return self._response_id

    @response_id.setter
    def response_id(self, value):
        self._response_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationUnofficialMaterialSubmitResponse, self).parse_response_content(response_content)
        if 'response_id' in response:
            self.response_id = response['response_id']
