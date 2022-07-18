#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DepartmentInfoDTO import DepartmentInfoDTO


class AlipayCommerceEcDepartmentInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcDepartmentInfoQueryResponse, self).__init__()
        self._department_info = None

    @property
    def department_info(self):
        return self._department_info

    @department_info.setter
    def department_info(self, value):
        if isinstance(value, DepartmentInfoDTO):
            self._department_info = value
        else:
            self._department_info = DepartmentInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcDepartmentInfoQueryResponse, self).parse_response_content(response_content)
        if 'department_info' in response:
            self.department_info = response['department_info']
