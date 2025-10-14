#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserPayDetail import UserPayDetail


class AlipayIserviceIssalaryPayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIssalaryPayQueryResponse, self).__init__()
        self._user_pay_details = None

    @property
    def user_pay_details(self):
        return self._user_pay_details

    @user_pay_details.setter
    def user_pay_details(self, value):
        if isinstance(value, list):
            self._user_pay_details = list()
            for i in value:
                if isinstance(i, UserPayDetail):
                    self._user_pay_details.append(i)
                else:
                    self._user_pay_details.append(UserPayDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIssalaryPayQueryResponse, self).parse_response_content(response_content)
        if 'user_pay_details' in response:
            self.user_pay_details = response['user_pay_details']
