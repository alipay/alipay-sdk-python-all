#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcardEduPublicBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcardEduPublicBindResponse, self).__init__()
        self._agent_code = None
        self._card_no = None
        self._return_code = None

    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcardEduPublicBindResponse, self).parse_response_content(response_content)
        if 'agent_code' in response:
            self.agent_code = response['agent_code']
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'return_code' in response:
            self.return_code = response['return_code']
