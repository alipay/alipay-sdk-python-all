#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmRobotSessionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmRobotSessionCreateResponse, self).__init__()
        self._session_id = None

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmRobotSessionCreateResponse, self).parse_response_content(response_content)
        if 'session_id' in response:
            self.session_id = response['session_id']
