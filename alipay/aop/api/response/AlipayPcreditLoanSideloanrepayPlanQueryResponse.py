#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MergedInstallmentBill import MergedInstallmentBill
from alipay.aop.api.domain.MergedInstallmentBill import MergedInstallmentBill
from alipay.aop.api.domain.InstallmentBill import InstallmentBill
from alipay.aop.api.domain.MergedInstallmentBill import MergedInstallmentBill


class AlipayPcreditLoanSideloanrepayPlanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanrepayPlanQueryResponse, self).__init__()
        self._due_merged_installment_bill = None
        self._following_merged_installment_bill = None
        self._installment_bill_list = None
        self._overdue_merged_installment_bill = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None
        self._unpaid_loan_total = None

    @property
    def due_merged_installment_bill(self):
        return self._due_merged_installment_bill

    @due_merged_installment_bill.setter
    def due_merged_installment_bill(self, value):
        if isinstance(value, MergedInstallmentBill):
            self._due_merged_installment_bill = value
        else:
            self._due_merged_installment_bill = MergedInstallmentBill.from_alipay_dict(value)
    @property
    def following_merged_installment_bill(self):
        return self._following_merged_installment_bill

    @following_merged_installment_bill.setter
    def following_merged_installment_bill(self, value):
        if isinstance(value, MergedInstallmentBill):
            self._following_merged_installment_bill = value
        else:
            self._following_merged_installment_bill = MergedInstallmentBill.from_alipay_dict(value)
    @property
    def installment_bill_list(self):
        return self._installment_bill_list

    @installment_bill_list.setter
    def installment_bill_list(self, value):
        if isinstance(value, list):
            self._installment_bill_list = list()
            for i in value:
                if isinstance(i, InstallmentBill):
                    self._installment_bill_list.append(i)
                else:
                    self._installment_bill_list.append(InstallmentBill.from_alipay_dict(i))
    @property
    def overdue_merged_installment_bill(self):
        return self._overdue_merged_installment_bill

    @overdue_merged_installment_bill.setter
    def overdue_merged_installment_bill(self, value):
        if isinstance(value, MergedInstallmentBill):
            self._overdue_merged_installment_bill = value
        else:
            self._overdue_merged_installment_bill = MergedInstallmentBill.from_alipay_dict(value)
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_sub_code(self):
        return self._return_sub_code

    @return_sub_code.setter
    def return_sub_code(self, value):
        self._return_sub_code = value
    @property
    def return_sub_message(self):
        return self._return_sub_message

    @return_sub_message.setter
    def return_sub_message(self, value):
        self._return_sub_message = value
    @property
    def unpaid_loan_total(self):
        return self._unpaid_loan_total

    @unpaid_loan_total.setter
    def unpaid_loan_total(self, value):
        self._unpaid_loan_total = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloanrepayPlanQueryResponse, self).parse_response_content(response_content)
        if 'due_merged_installment_bill' in response:
            self.due_merged_installment_bill = response['due_merged_installment_bill']
        if 'following_merged_installment_bill' in response:
            self.following_merged_installment_bill = response['following_merged_installment_bill']
        if 'installment_bill_list' in response:
            self.installment_bill_list = response['installment_bill_list']
        if 'overdue_merged_installment_bill' in response:
            self.overdue_merged_installment_bill = response['overdue_merged_installment_bill']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
        if 'unpaid_loan_total' in response:
            self.unpaid_loan_total = response['unpaid_loan_total']
