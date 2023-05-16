#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotvspUserstateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspUserstateQueryResponse, self).__init__()
        self._group_state = None
        self._state = None

    @property
    def group_state(self):
        return self._group_state

    @group_state.setter
    def group_state(self, value):
        self._group_state = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspUserstateQueryResponse, self).parse_response_content(response_content)
        if 'group_state' in response:
            self.group_state = response['group_state']
        if 'state' in response:
            self.state = response['state']
