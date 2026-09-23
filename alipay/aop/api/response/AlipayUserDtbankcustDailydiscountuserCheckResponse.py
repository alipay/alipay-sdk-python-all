#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankcustDailydiscountuserCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankcustDailydiscountuserCheckResponse, self).__init__()
        self._pre_registration_status = None

    @property
    def pre_registration_status(self):
        return self._pre_registration_status

    @pre_registration_status.setter
    def pre_registration_status(self, value):
        self._pre_registration_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankcustDailydiscountuserCheckResponse, self).parse_response_content(response_content)
        if 'pre_registration_status' in response:
            self.pre_registration_status = response['pre_registration_status']
