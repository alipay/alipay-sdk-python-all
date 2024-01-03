#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGameopenpromoChallengeSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGameopenpromoChallengeSubmitResponse, self).__init__()
        self._submit_status = None

    @property
    def submit_status(self):
        return self._submit_status

    @submit_status.setter
    def submit_status(self, value):
        self._submit_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGameopenpromoChallengeSubmitResponse, self).parse_response_content(response_content)
        if 'submit_status' in response:
            self.submit_status = response['submit_status']
