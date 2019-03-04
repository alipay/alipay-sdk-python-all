#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserPermit import UserPermit


class AlipayEcoCityservicePushmsgPermitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityservicePushmsgPermitQueryResponse, self).__init__()
        self._user_permit_list = None

    @property
    def user_permit_list(self):
        return self._user_permit_list

    @user_permit_list.setter
    def user_permit_list(self, value):
        if isinstance(value, list):
            self._user_permit_list = list()
            for i in value:
                if isinstance(i, UserPermit):
                    self._user_permit_list.append(i)
                else:
                    self._user_permit_list.append(UserPermit.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityservicePushmsgPermitQueryResponse, self).parse_response_content(response_content)
        if 'user_permit_list' in response:
            self.user_permit_list = response['user_permit_list']
