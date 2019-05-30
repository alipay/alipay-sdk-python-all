#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMemberSceneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMemberSceneQueryResponse, self).__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserMemberSceneQueryResponse, self).parse_response_content(response_content)
        if 'state' in response:
            self.state = response['state']
