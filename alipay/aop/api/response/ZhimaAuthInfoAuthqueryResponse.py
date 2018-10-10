#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaAuthInfoAuthqueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaAuthInfoAuthqueryResponse, self).__init__()
        self._authorized = None
        self._open_id = None

    @property
    def authorized(self):
        return self._authorized

    @authorized.setter
    def authorized(self, value):
        self._authorized = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaAuthInfoAuthqueryResponse, self).parse_response_content(response_content)
        if 'authorized' in response:
            self.authorized = response['authorized']
        if 'open_id' in response:
            self.open_id = response['open_id']
