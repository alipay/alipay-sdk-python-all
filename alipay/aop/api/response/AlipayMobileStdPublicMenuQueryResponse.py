#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobileStdPublicMenuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileStdPublicMenuQueryResponse, self).__init__()
        self._all_menu_list = None

    @property
    def all_menu_list(self):
        return self._all_menu_list

    @all_menu_list.setter
    def all_menu_list(self, value):
        self._all_menu_list = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileStdPublicMenuQueryResponse, self).parse_response_content(response_content)
        if 'all_menu_list' in response:
            self.all_menu_list = response['all_menu_list']
