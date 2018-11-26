#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserLoginStatusDetail import UserLoginStatusDetail


class KoubeiMerchantKbcloudSubuserloginstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantKbcloudSubuserloginstatusQueryResponse, self).__init__()
        self._user_login_status = None

    @property
    def user_login_status(self):
        return self._user_login_status

    @user_login_status.setter
    def user_login_status(self, value):
        if isinstance(value, UserLoginStatusDetail):
            self._user_login_status = value
        else:
            self._user_login_status = UserLoginStatusDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantKbcloudSubuserloginstatusQueryResponse, self).parse_response_content(response_content)
        if 'user_login_status' in response:
            self.user_login_status = response['user_login_status']
