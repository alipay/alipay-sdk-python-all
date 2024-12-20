#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SideloanInstitution import SideloanInstitution
from alipay.aop.api.domain.InstallmentPlan import InstallmentPlan


class AlipayPcreditLoanSideloanlendCalcConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanlendCalcConsultResponse, self).__init__()
        self._credit_quota = None
        self._daily_interest_rate = None
        self._extension = None
        self._fund_supplier = None
        self._installment_plan_list = None
        self._interest = None
        self._interest_rate = None
        self._principal = None
        self._promotion_amount = None
        self._repayment_day = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None
        self._surplus_quota = None
        self._total_amount = None

    @property
    def credit_quota(self):
        return self._credit_quota

    @credit_quota.setter
    def credit_quota(self, value):
        self._credit_quota = value
    @property
    def daily_interest_rate(self):
        return self._daily_interest_rate

    @daily_interest_rate.setter
    def daily_interest_rate(self, value):
        self._daily_interest_rate = value
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def fund_supplier(self):
        return self._fund_supplier

    @fund_supplier.setter
    def fund_supplier(self, value):
        if isinstance(value, SideloanInstitution):
            self._fund_supplier = value
        else:
            self._fund_supplier = SideloanInstitution.from_alipay_dict(value)
    @property
    def installment_plan_list(self):
        return self._installment_plan_list

    @installment_plan_list.setter
    def installment_plan_list(self, value):
        if isinstance(value, list):
            self._installment_plan_list = list()
            for i in value:
                if isinstance(i, InstallmentPlan):
                    self._installment_plan_list.append(i)
                else:
                    self._installment_plan_list.append(InstallmentPlan.from_alipay_dict(i))
    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value
    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def promotion_amount(self):
        return self._promotion_amount

    @promotion_amount.setter
    def promotion_amount(self, value):
        self._promotion_amount = value
    @property
    def repayment_day(self):
        return self._repayment_day

    @repayment_day.setter
    def repayment_day(self, value):
        self._repayment_day = value
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
    def surplus_quota(self):
        return self._surplus_quota

    @surplus_quota.setter
    def surplus_quota(self, value):
        self._surplus_quota = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloanlendCalcConsultResponse, self).parse_response_content(response_content)
        if 'credit_quota' in response:
            self.credit_quota = response['credit_quota']
        if 'daily_interest_rate' in response:
            self.daily_interest_rate = response['daily_interest_rate']
        if 'extension' in response:
            self.extension = response['extension']
        if 'fund_supplier' in response:
            self.fund_supplier = response['fund_supplier']
        if 'installment_plan_list' in response:
            self.installment_plan_list = response['installment_plan_list']
        if 'interest' in response:
            self.interest = response['interest']
        if 'interest_rate' in response:
            self.interest_rate = response['interest_rate']
        if 'principal' in response:
            self.principal = response['principal']
        if 'promotion_amount' in response:
            self.promotion_amount = response['promotion_amount']
        if 'repayment_day' in response:
            self.repayment_day = response['repayment_day']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
        if 'surplus_quota' in response:
            self.surplus_quota = response['surplus_quota']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
