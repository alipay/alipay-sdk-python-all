#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DepartmentInfoVO import DepartmentInfoVO


class AlipayCommerceMedicalSearchDepartmentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalSearchDepartmentQueryResponse, self).__init__()
        self._depart_list = None

    @property
    def depart_list(self):
        return self._depart_list

    @depart_list.setter
    def depart_list(self, value):
        if isinstance(value, DepartmentInfoVO):
            self._depart_list = value
        else:
            self._depart_list = DepartmentInfoVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalSearchDepartmentQueryResponse, self).parse_response_content(response_content)
        if 'depart_list' in response:
            self.depart_list = response['depart_list']
