#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountSchoolAccountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountSchoolAccountConsultResponse, self).__init__()
        self._has_registered = None

    @property
    def has_registered(self):
        return self._has_registered

    @has_registered.setter
    def has_registered(self, value):
        self._has_registered = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountSchoolAccountConsultResponse, self).parse_response_content(response_content)
        if 'has_registered' in response:
            self.has_registered = response['has_registered']
