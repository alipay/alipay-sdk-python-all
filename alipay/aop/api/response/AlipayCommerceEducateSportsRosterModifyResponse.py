#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSportsRosterModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSportsRosterModifyResponse, self).__init__()
        self._roster_code = None

    @property
    def roster_code(self):
        return self._roster_code

    @roster_code.setter
    def roster_code(self, value):
        self._roster_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSportsRosterModifyResponse, self).parse_response_content(response_content)
        if 'roster_code' in response:
            self.roster_code = response['roster_code']
