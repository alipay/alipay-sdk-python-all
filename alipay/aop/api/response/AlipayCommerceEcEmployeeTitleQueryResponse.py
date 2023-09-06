#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EmployeeTitleInfoDTO import EmployeeTitleInfoDTO


class AlipayCommerceEcEmployeeTitleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeTitleQueryResponse, self).__init__()
        self._employee_title_list = None

    @property
    def employee_title_list(self):
        return self._employee_title_list

    @employee_title_list.setter
    def employee_title_list(self, value):
        if isinstance(value, EmployeeTitleInfoDTO):
            self._employee_title_list = value
        else:
            self._employee_title_list = EmployeeTitleInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeTitleQueryResponse, self).parse_response_content(response_content)
        if 'employee_title_list' in response:
            self.employee_title_list = response['employee_title_list']
