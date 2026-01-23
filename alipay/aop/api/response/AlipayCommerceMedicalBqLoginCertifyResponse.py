#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BianQueUserAuthDetail import BianQueUserAuthDetail


class AlipayCommerceMedicalBqLoginCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalBqLoginCertifyResponse, self).__init__()
        self._user_auth_detail = None

    @property
    def user_auth_detail(self):
        return self._user_auth_detail

    @user_auth_detail.setter
    def user_auth_detail(self, value):
        if isinstance(value, BianQueUserAuthDetail):
            self._user_auth_detail = value
        else:
            self._user_auth_detail = BianQueUserAuthDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalBqLoginCertifyResponse, self).parse_response_content(response_content)
        if 'user_auth_detail' in response:
            self.user_auth_detail = response['user_auth_detail']
