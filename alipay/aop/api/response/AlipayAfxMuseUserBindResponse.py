#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAfxMuseUserBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAfxMuseUserBindResponse, self).__init__()
        self._muse_session_id = None

    @property
    def muse_session_id(self):
        return self._muse_session_id

    @muse_session_id.setter
    def muse_session_id(self, value):
        self._muse_session_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayAfxMuseUserBindResponse, self).parse_response_content(response_content)
        if 'muse_session_id' in response:
            self.muse_session_id = response['muse_session_id']
