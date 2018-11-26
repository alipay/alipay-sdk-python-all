#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserInvitetaskExchangeConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInvitetaskExchangeConfirmResponse, self).__init__()
        self._confirm_result = None

    @property
    def confirm_result(self):
        return self._confirm_result

    @confirm_result.setter
    def confirm_result(self, value):
        self._confirm_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserInvitetaskExchangeConfirmResponse, self).parse_response_content(response_content)
        if 'confirm_result' in response:
            self.confirm_result = response['confirm_result']
