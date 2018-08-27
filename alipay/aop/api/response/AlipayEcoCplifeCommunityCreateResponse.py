#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCplifeCommunityCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeCommunityCreateResponse, self).__init__()
        self._community_id = None
        self._next_action = None
        self._status = None

    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def next_action(self):
        return self._next_action

    @next_action.setter
    def next_action(self, value):
        self._next_action = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeCommunityCreateResponse, self).parse_response_content(response_content)
        if 'community_id' in response:
            self.community_id = response['community_id']
        if 'next_action' in response:
            self.next_action = response['next_action']
        if 'status' in response:
            self.status = response['status']
