#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicMenuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicMenuQueryResponse, self).__init__()
        self._menu_content = None

    @property
    def menu_content(self):
        return self._menu_content

    @menu_content.setter
    def menu_content(self, value):
        self._menu_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicMenuQueryResponse, self).parse_response_content(response_content)
        if 'menu_content' in response:
            self.menu_content = response['menu_content']
