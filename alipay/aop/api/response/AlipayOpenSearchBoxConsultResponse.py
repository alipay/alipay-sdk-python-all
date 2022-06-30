#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSearchBoxConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchBoxConsultResponse, self).__init__()
        self._access = None
        self._not_pass_items = None

    @property
    def access(self):
        return self._access

    @access.setter
    def access(self, value):
        self._access = value
    @property
    def not_pass_items(self):
        return self._not_pass_items

    @not_pass_items.setter
    def not_pass_items(self, value):
        if isinstance(value, list):
            self._not_pass_items = list()
            for i in value:
                self._not_pass_items.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchBoxConsultResponse, self).parse_response_content(response_content)
        if 'access' in response:
            self.access = response['access']
        if 'not_pass_items' in response:
            self.not_pass_items = response['not_pass_items']
