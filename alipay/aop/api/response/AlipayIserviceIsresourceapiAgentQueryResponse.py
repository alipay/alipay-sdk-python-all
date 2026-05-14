#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceIsresourceapiAgentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIsresourceapiAgentQueryResponse, self).__init__()
        self._exists = None

    @property
    def exists(self):
        return self._exists

    @exists.setter
    def exists(self, value):
        self._exists = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIsresourceapiAgentQueryResponse, self).parse_response_content(response_content)
        if 'exists' in response:
            self.exists = response['exists']
