#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayUserCustIdentifyActivity import AlipayUserCustIdentifyActivity


class AlipayUserCustomerIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCustomerIdentifyResponse, self).__init__()
        self._activity_list = None
        self._user_profile = None

    @property
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        if isinstance(value, list):
            self._activity_list = list()
            for i in value:
                if isinstance(i, AlipayUserCustIdentifyActivity):
                    self._activity_list.append(i)
                else:
                    self._activity_list.append(AlipayUserCustIdentifyActivity.from_alipay_dict(i))
    @property
    def user_profile(self):
        return self._user_profile

    @user_profile.setter
    def user_profile(self, value):
        self._user_profile = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCustomerIdentifyResponse, self).parse_response_content(response_content)
        if 'activity_list' in response:
            self.activity_list = response['activity_list']
        if 'user_profile' in response:
            self.user_profile = response['user_profile']
