#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityAccessUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityAccessUploadResponse, self).__init__()
        self._mobile = None
        self._reason = None
        self._user_name = None

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityAccessUploadResponse, self).parse_response_content(response_content)
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'reason' in response:
            self.reason = response['reason']
        if 'user_name' in response:
            self.user_name = response['user_name']
