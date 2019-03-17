#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoUserMsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoUserMsgSendResponse, self).__init__()
        self._can_retry = None

    @property
    def can_retry(self):
        return self._can_retry

    @can_retry.setter
    def can_retry(self, value):
        self._can_retry = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoUserMsgSendResponse, self).parse_response_content(response_content)
        if 'can_retry' in response:
            self.can_retry = response['can_retry']
