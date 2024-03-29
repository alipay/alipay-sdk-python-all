#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAccountUseridBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountUseridBatchqueryResponse, self).__init__()
        self._open_id_list = None
        self._user_id_list = None

    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                self._open_id_list.append(i)
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
        response = super(AlipayUserAccountUseridBatchqueryResponse, self).parse_response_content(response_content)
        if 'open_id_list' in response:
            self.open_id_list = response['open_id_list']
        if 'user_id_list' in response:
            self.user_id_list = response['user_id_list']
