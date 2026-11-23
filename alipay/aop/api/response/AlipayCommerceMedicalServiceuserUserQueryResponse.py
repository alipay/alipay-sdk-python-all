#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserRef import UserRef


class AlipayCommerceMedicalServiceuserUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServiceuserUserQueryResponse, self).__init__()
        self._user_ref_list = None

    @property
    def user_ref_list(self):
        return self._user_ref_list

    @user_ref_list.setter
    def user_ref_list(self, value):
        if isinstance(value, list):
            self._user_ref_list = list()
            for i in value:
                if isinstance(i, UserRef):
                    self._user_ref_list.append(i)
                else:
                    self._user_ref_list.append(UserRef.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServiceuserUserQueryResponse, self).parse_response_content(response_content)
        if 'user_ref_list' in response:
            self.user_ref_list = response['user_ref_list']
