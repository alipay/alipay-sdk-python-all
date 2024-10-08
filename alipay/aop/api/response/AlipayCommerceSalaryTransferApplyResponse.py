#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SalaryApplySignData import SalaryApplySignData


class AlipayCommerceSalaryTransferApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSalaryTransferApplyResponse, self).__init__()
        self._apply_time = None
        self._salary_order_id = None
        self._sign_data = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def salary_order_id(self):
        return self._salary_order_id

    @salary_order_id.setter
    def salary_order_id(self, value):
        self._salary_order_id = value
    @property
    def sign_data(self):
        return self._sign_data

    @sign_data.setter
    def sign_data(self, value):
        if isinstance(value, SalaryApplySignData):
            self._sign_data = value
        else:
            self._sign_data = SalaryApplySignData.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSalaryTransferApplyResponse, self).parse_response_content(response_content)
        if 'apply_time' in response:
            self.apply_time = response['apply_time']
        if 'salary_order_id' in response:
            self.salary_order_id = response['salary_order_id']
        if 'sign_data' in response:
            self.sign_data = response['sign_data']
