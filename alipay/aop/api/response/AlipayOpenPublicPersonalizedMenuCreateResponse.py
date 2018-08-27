#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicPersonalizedMenuCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicPersonalizedMenuCreateResponse, self).__init__()
        self._menu_key = None

    @property
    def menu_key(self):
        return self._menu_key

    @menu_key.setter
    def menu_key(self, value):
        self._menu_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicPersonalizedMenuCreateResponse, self).parse_response_content(response_content)
        if 'menu_key' in response:
            self.menu_key = response['menu_key']
