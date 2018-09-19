#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicFollowBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicFollowBatchqueryResponse, self).__init__()
        self._count = None
        self._next_user_id = None
        self._user_id_list = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def next_user_id(self):
        return self._next_user_id

    @next_user_id.setter
    def next_user_id(self, value):
        self._next_user_id = value
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
        response = super(AlipayOpenPublicFollowBatchqueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'next_user_id' in response:
            self.next_user_id = response['next_user_id']
        if 'user_id_list' in response:
            self.user_id_list = response['user_id_list']
