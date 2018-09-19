#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DepartmentDTO import DepartmentDTO


class KoubeiMerchantDepartmentTreeQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantDepartmentTreeQueryResponse, self).__init__()
        self._department_dtos = None

    @property
    def department_dtos(self):
        return self._department_dtos

    @department_dtos.setter
    def department_dtos(self, value):
        if isinstance(value, list):
            self._department_dtos = list()
            for i in value:
                if isinstance(i, DepartmentDTO):
                    self._department_dtos.append(i)
                else:
                    self._department_dtos.append(DepartmentDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantDepartmentTreeQueryResponse, self).parse_response_content(response_content)
        if 'department_dtos' in response:
            self.department_dtos = response['department_dtos']
