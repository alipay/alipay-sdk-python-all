#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EmployeeInfoDTO import EmployeeInfoDTO


class AlipayCommerceEcEmployeeInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeInfoQueryResponse, self).__init__()
        self._employee_info = None

    @property
    def employee_info(self):
        return self._employee_info

    @employee_info.setter
    def employee_info(self, value):
        if isinstance(value, EmployeeInfoDTO):
            self._employee_info = value
        else:
            self._employee_info = EmployeeInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeInfoQueryResponse, self).parse_response_content(response_content)
        if 'employee_info' in response:
            self.employee_info = response['employee_info']
