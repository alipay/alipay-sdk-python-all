#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotMembershipcouponQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotMembershipcouponQueryResponse, self).__init__()
        self._activity_id = None
        self._auth_pid = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def auth_pid(self):
        return self._auth_pid

    @auth_pid.setter
    def auth_pid(self, value):
        self._auth_pid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotMembershipcouponQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'auth_pid' in response:
            self.auth_pid = response['auth_pid']
