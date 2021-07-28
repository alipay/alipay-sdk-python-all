#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserIdentityInfo import UserIdentityInfo


class AlipayUserTwostageCommonUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserTwostageCommonUseResponse, self).__init__()
        self._user_id = None
        self._user_identity_info = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_identity_info(self):
        return self._user_identity_info

    @user_identity_info.setter
    def user_identity_info(self, value):
        if isinstance(value, UserIdentityInfo):
            self._user_identity_info = value
        else:
            self._user_identity_info = UserIdentityInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserTwostageCommonUseResponse, self).parse_response_content(response_content)
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_identity_info' in response:
            self.user_identity_info = response['user_identity_info']
