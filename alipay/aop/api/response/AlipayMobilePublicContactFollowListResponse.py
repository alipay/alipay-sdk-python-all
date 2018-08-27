#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicContactFollowListResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicContactFollowListResponse, self).__init__()
        self._code = None
        self._contact_follow_list = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def contact_follow_list(self):
        return self._contact_follow_list

    @contact_follow_list.setter
    def contact_follow_list(self, value):
        if isinstance(value, list):
            self._contact_follow_list = list()
            for i in value:
                self._contact_follow_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicContactFollowListResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'contact_follow_list' in response:
            self.contact_follow_list = response['contact_follow_list']
