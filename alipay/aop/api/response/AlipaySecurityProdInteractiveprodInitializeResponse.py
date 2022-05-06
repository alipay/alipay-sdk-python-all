#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdInteractiveprodInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdInteractiveprodInitializeResponse, self).__init__()
        self._ext_params = None
        self._interact_id = None
        self._interact_url = None

    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def interact_id(self):
        return self._interact_id

    @interact_id.setter
    def interact_id(self, value):
        self._interact_id = value
    @property
    def interact_url(self):
        return self._interact_url

    @interact_url.setter
    def interact_url(self, value):
        self._interact_url = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdInteractiveprodInitializeResponse, self).parse_response_content(response_content)
        if 'ext_params' in response:
            self.ext_params = response['ext_params']
        if 'interact_id' in response:
            self.interact_id = response['interact_id']
        if 'interact_url' in response:
            self.interact_url = response['interact_url']
