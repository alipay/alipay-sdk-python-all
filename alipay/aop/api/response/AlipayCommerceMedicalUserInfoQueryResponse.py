#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserQueryInfo import UserQueryInfo


class AlipayCommerceMedicalUserInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalUserInfoQueryResponse, self).__init__()
        self._user_query_info = None

    @property
    def user_query_info(self):
        return self._user_query_info

    @user_query_info.setter
    def user_query_info(self, value):
        if isinstance(value, UserQueryInfo):
            self._user_query_info = value
        else:
            self._user_query_info = UserQueryInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalUserInfoQueryResponse, self).parse_response_content(response_content)
        if 'user_query_info' in response:
            self.user_query_info = response['user_query_info']
