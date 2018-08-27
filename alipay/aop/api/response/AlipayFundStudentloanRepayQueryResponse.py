#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RepayDetail import RepayDetail


class AlipayFundStudentloanRepayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundStudentloanRepayQueryResponse, self).__init__()
        self._biz_type = None
        self._branch_name = None
        self._org_name = None
        self._repay_date = None
        self._repay_list = None
        self._should_amount = None
        self._student_name = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def repay_list(self):
        return self._repay_list

    @repay_list.setter
    def repay_list(self, value):
        if isinstance(value, list):
            self._repay_list = list()
            for i in value:
                if isinstance(i, RepayDetail):
                    self._repay_list.append(i)
                else:
                    self._repay_list.append(RepayDetail.from_alipay_dict(i))
    @property
    def should_amount(self):
        return self._should_amount

    @should_amount.setter
    def should_amount(self, value):
        self._should_amount = value
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundStudentloanRepayQueryResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'branch_name' in response:
            self.branch_name = response['branch_name']
        if 'org_name' in response:
            self.org_name = response['org_name']
        if 'repay_date' in response:
            self.repay_date = response['repay_date']
        if 'repay_list' in response:
            self.repay_list = response['repay_list']
        if 'should_amount' in response:
            self.should_amount = response['should_amount']
        if 'student_name' in response:
            self.student_name = response['student_name']
