#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicPartnerMenuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicPartnerMenuQueryResponse, self).__init__()
        self._public_menu = None

    @property
    def public_menu(self):
        return self._public_menu

    @public_menu.setter
    def public_menu(self, value):
        self._public_menu = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicPartnerMenuQueryResponse, self).parse_response_content(response_content)
        if 'public_menu' in response:
            self.public_menu = response['public_menu']
