#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAuthOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAuthOrderCloseResponse, self).__init__()
        self._auth_opt_id = None
        self._out_request_no = None

    @property
    def auth_opt_id(self):
        return self._auth_opt_id

    @auth_opt_id.setter
    def auth_opt_id(self, value):
        self._auth_opt_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAuthOrderCloseResponse, self).parse_response_content(response_content)
        if 'auth_opt_id' in response:
            self.auth_opt_id = response['auth_opt_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
