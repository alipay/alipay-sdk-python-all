#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DepartmentLabel import DepartmentLabel


class KoubeiMerchantDepartmentLabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantDepartmentLabelQueryResponse, self).__init__()
        self._department_labels = None

    @property
    def department_labels(self):
        return self._department_labels

    @department_labels.setter
    def department_labels(self, value):
        if isinstance(value, list):
            self._department_labels = list()
            for i in value:
                if isinstance(i, DepartmentLabel):
                    self._department_labels.append(i)
                else:
                    self._department_labels.append(DepartmentLabel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantDepartmentLabelQueryResponse, self).parse_response_content(response_content)
        if 'department_labels' in response:
            self.department_labels = response['department_labels']
