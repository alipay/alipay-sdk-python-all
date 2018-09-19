#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGroupshoppingNewbieQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGroupshoppingNewbieQueryResponse, self).__init__()
        self._access = None
        self._message = None
        self._reason = None
        self._user_id_list = None

    @property
    def access(self):
        return self._access

    @access.setter
    def access(self, value):
        self._access = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def user_id_list(self):
        return self._user_id_list

    @user_id_list.setter
    def user_id_list(self, value):
        if isinstance(value, list):
            self._user_id_list = list()
            for i in value:
                self._user_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayUserGroupshoppingNewbieQueryResponse, self).parse_response_content(response_content)
        if 'access' in response:
            self.access = response['access']
        if 'message' in response:
            self.message = response['message']
        if 'reason' in response:
            self.reason = response['reason']
        if 'user_id_list' in response:
            self.user_id_list = response['user_id_list']
