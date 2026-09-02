#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCreditBankcardBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCreditBankcardBindResponse, self).__init__()
        self._schema = None

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value):
        self._schema = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCreditBankcardBindResponse, self).parse_response_content(response_content)
        if 'schema' in response:
            self.schema = response['schema']
