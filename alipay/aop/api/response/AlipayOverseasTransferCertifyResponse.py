#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTransferCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTransferCertifyResponse, self).__init__()
        self._has_default_card = None
        self._pass_through_info = None

    @property
    def has_default_card(self):
        return self._has_default_card

    @has_default_card.setter
    def has_default_card(self, value):
        self._has_default_card = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTransferCertifyResponse, self).parse_response_content(response_content)
        if 'has_default_card' in response:
            self.has_default_card = response['has_default_card']
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']
