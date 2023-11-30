#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcTransAccountBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTransAccountBindResponse, self).__init__()
        self._authorize_link = None

    @property
    def authorize_link(self):
        return self._authorize_link

    @authorize_link.setter
    def authorize_link(self, value):
        self._authorize_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTransAccountBindResponse, self).parse_response_content(response_content)
        if 'authorize_link' in response:
            self.authorize_link = response['authorize_link']
