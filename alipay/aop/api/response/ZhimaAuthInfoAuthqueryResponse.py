#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaAuthInfoAuthqueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaAuthInfoAuthqueryResponse, self).__init__()
        self._authorized = None

    @property
    def authorized(self):
        return self._authorized

    @authorized.setter
    def authorized(self, value):
        self._authorized = value

    def parse_response_content(self, response_content):
        response = super(ZhimaAuthInfoAuthqueryResponse, self).parse_response_content(response_content)
        if 'authorized' in response:
            self.authorized = response['authorized']
