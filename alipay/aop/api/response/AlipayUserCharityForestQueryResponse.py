#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCharityForestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCharityForestQueryResponse, self).__init__()
        self._forest_user = None

    @property
    def forest_user(self):
        return self._forest_user

    @forest_user.setter
    def forest_user(self, value):
        self._forest_user = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCharityForestQueryResponse, self).parse_response_content(response_content)
        if 'forest_user' in response:
            self.forest_user = response['forest_user']
