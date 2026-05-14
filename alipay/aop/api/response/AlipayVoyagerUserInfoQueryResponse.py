#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoyagerUserInfo import VoyagerUserInfo


class AlipayVoyagerUserInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerUserInfoQueryResponse, self).__init__()
        self._user_info = None

    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, VoyagerUserInfo):
            self._user_info = value
        else:
            self._user_info = VoyagerUserInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerUserInfoQueryResponse, self).parse_response_content(response_content)
        if 'user_info' in response:
            self.user_info = response['user_info']
