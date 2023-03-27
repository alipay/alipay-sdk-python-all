#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcEmployeeBatchAddFailInfo import EcEmployeeBatchAddFailInfo
from alipay.aop.api.domain.EcEmployeeBatchAddSuccessInfo import EcEmployeeBatchAddSuccessInfo


class AlipayCommerceEcEmployeeBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeBatchcreateResponse, self).__init__()
        self._employee_add_fail_list = None
        self._employee_add_success_list = None
        self._sign_url = None

    @property
    def employee_add_fail_list(self):
        return self._employee_add_fail_list

    @employee_add_fail_list.setter
    def employee_add_fail_list(self, value):
        if isinstance(value, list):
            self._employee_add_fail_list = list()
            for i in value:
                if isinstance(i, EcEmployeeBatchAddFailInfo):
                    self._employee_add_fail_list.append(i)
                else:
                    self._employee_add_fail_list.append(EcEmployeeBatchAddFailInfo.from_alipay_dict(i))
    @property
    def employee_add_success_list(self):
        return self._employee_add_success_list

    @employee_add_success_list.setter
    def employee_add_success_list(self, value):
        if isinstance(value, list):
            self._employee_add_success_list = list()
            for i in value:
                if isinstance(i, EcEmployeeBatchAddSuccessInfo):
                    self._employee_add_success_list.append(i)
                else:
                    self._employee_add_success_list.append(EcEmployeeBatchAddSuccessInfo.from_alipay_dict(i))
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeBatchcreateResponse, self).parse_response_content(response_content)
        if 'employee_add_fail_list' in response:
            self.employee_add_fail_list = response['employee_add_fail_list']
        if 'employee_add_success_list' in response:
            self.employee_add_success_list = response['employee_add_success_list']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
