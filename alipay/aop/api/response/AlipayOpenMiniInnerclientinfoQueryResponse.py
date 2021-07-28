#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerclientinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerclientinfoQueryResponse, self).__init__()
        self._bundle_id = None
        self._bundle_name = None
        self._client_id = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def bundle_name(self):
        return self._bundle_name

    @bundle_name.setter
    def bundle_name(self, value):
        self._bundle_name = value
    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerclientinfoQueryResponse, self).parse_response_content(response_content)
        if 'bundle_id' in response:
            self.bundle_id = response['bundle_id']
        if 'bundle_name' in response:
            self.bundle_name = response['bundle_name']
        if 'client_id' in response:
            self.client_id = response['client_id']
