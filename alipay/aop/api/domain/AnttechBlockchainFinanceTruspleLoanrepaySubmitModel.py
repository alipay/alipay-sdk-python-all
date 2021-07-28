#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstallmentDetail import InstallmentDetail


class AnttechBlockchainFinanceTruspleLoanrepaySubmitModel(object):

    def __init__(self):
        self._actual_repaid_amount = None
        self._external_loan_id = None
        self._external_repay_request_id = None
        self._external_user_id = None
        self._fund_channel = None
        self._fund_message = None
        self._inst_code = None
        self._installment_details = None
        self._repay_amount_currency = None
        self._repay_time = None
        self._repay_type = None

    @property
    def actual_repaid_amount(self):
        return self._actual_repaid_amount

    @actual_repaid_amount.setter
    def actual_repaid_amount(self, value):
        self._actual_repaid_amount = value
    @property
    def external_loan_id(self):
        return self._external_loan_id

    @external_loan_id.setter
    def external_loan_id(self, value):
        self._external_loan_id = value
    @property
    def external_repay_request_id(self):
        return self._external_repay_request_id

    @external_repay_request_id.setter
    def external_repay_request_id(self, value):
        self._external_repay_request_id = value
    @property
    def external_user_id(self):
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, value):
        self._external_user_id = value
    @property
    def fund_channel(self):
        return self._fund_channel

    @fund_channel.setter
    def fund_channel(self, value):
        self._fund_channel = value
    @property
    def fund_message(self):
        return self._fund_message

    @fund_message.setter
    def fund_message(self, value):
        self._fund_message = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def installment_details(self):
        return self._installment_details

    @installment_details.setter
    def installment_details(self, value):
        if isinstance(value, list):
            self._installment_details = list()
            for i in value:
                if isinstance(i, InstallmentDetail):
                    self._installment_details.append(i)
                else:
                    self._installment_details.append(InstallmentDetail.from_alipay_dict(i))
    @property
    def repay_amount_currency(self):
        return self._repay_amount_currency

    @repay_amount_currency.setter
    def repay_amount_currency(self, value):
        self._repay_amount_currency = value
    @property
    def repay_time(self):
        return self._repay_time

    @repay_time.setter
    def repay_time(self, value):
        self._repay_time = value
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_repaid_amount:
            if hasattr(self.actual_repaid_amount, 'to_alipay_dict'):
                params['actual_repaid_amount'] = self.actual_repaid_amount.to_alipay_dict()
            else:
                params['actual_repaid_amount'] = self.actual_repaid_amount
        if self.external_loan_id:
            if hasattr(self.external_loan_id, 'to_alipay_dict'):
                params['external_loan_id'] = self.external_loan_id.to_alipay_dict()
            else:
                params['external_loan_id'] = self.external_loan_id
        if self.external_repay_request_id:
            if hasattr(self.external_repay_request_id, 'to_alipay_dict'):
                params['external_repay_request_id'] = self.external_repay_request_id.to_alipay_dict()
            else:
                params['external_repay_request_id'] = self.external_repay_request_id
        if self.external_user_id:
            if hasattr(self.external_user_id, 'to_alipay_dict'):
                params['external_user_id'] = self.external_user_id.to_alipay_dict()
            else:
                params['external_user_id'] = self.external_user_id
        if self.fund_channel:
            if hasattr(self.fund_channel, 'to_alipay_dict'):
                params['fund_channel'] = self.fund_channel.to_alipay_dict()
            else:
                params['fund_channel'] = self.fund_channel
        if self.fund_message:
            if hasattr(self.fund_message, 'to_alipay_dict'):
                params['fund_message'] = self.fund_message.to_alipay_dict()
            else:
                params['fund_message'] = self.fund_message
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.installment_details:
            if isinstance(self.installment_details, list):
                for i in range(0, len(self.installment_details)):
                    element = self.installment_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installment_details[i] = element.to_alipay_dict()
            if hasattr(self.installment_details, 'to_alipay_dict'):
                params['installment_details'] = self.installment_details.to_alipay_dict()
            else:
                params['installment_details'] = self.installment_details
        if self.repay_amount_currency:
            if hasattr(self.repay_amount_currency, 'to_alipay_dict'):
                params['repay_amount_currency'] = self.repay_amount_currency.to_alipay_dict()
            else:
                params['repay_amount_currency'] = self.repay_amount_currency
        if self.repay_time:
            if hasattr(self.repay_time, 'to_alipay_dict'):
                params['repay_time'] = self.repay_time.to_alipay_dict()
            else:
                params['repay_time'] = self.repay_time
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTruspleLoanrepaySubmitModel()
        if 'actual_repaid_amount' in d:
            o.actual_repaid_amount = d['actual_repaid_amount']
        if 'external_loan_id' in d:
            o.external_loan_id = d['external_loan_id']
        if 'external_repay_request_id' in d:
            o.external_repay_request_id = d['external_repay_request_id']
        if 'external_user_id' in d:
            o.external_user_id = d['external_user_id']
        if 'fund_channel' in d:
            o.fund_channel = d['fund_channel']
        if 'fund_message' in d:
            o.fund_message = d['fund_message']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'installment_details' in d:
            o.installment_details = d['installment_details']
        if 'repay_amount_currency' in d:
            o.repay_amount_currency = d['repay_amount_currency']
        if 'repay_time' in d:
            o.repay_time = d['repay_time']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        return o


