#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcEmployeeTitleFailed import EcEmployeeTitleFailed


class AlipayCommerceEcEmployeeTitleDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeTitleDeleteResponse, self).__init__()
        self._ec_employee_title_failed_list = None

    @property
    def ec_employee_title_failed_list(self):
        return self._ec_employee_title_failed_list

    @ec_employee_title_failed_list.setter
    def ec_employee_title_failed_list(self, value):
        if isinstance(value, EcEmployeeTitleFailed):
            self._ec_employee_title_failed_list = value
        else:
            self._ec_employee_title_failed_list = EcEmployeeTitleFailed.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeTitleDeleteResponse, self).parse_response_content(response_content)
        if 'ec_employee_title_failed_list' in response:
            self.ec_employee_title_failed_list = response['ec_employee_title_failed_list']
