#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerLoanBillLoanRelation import ConsumerLoanBillLoanRelation


class ConsumerLoanBillInfoItem(object):

    def __init__(self):
        self._allowed_pay_off_early_date = None
        self._bill_id = None
        self._commission_amount = None
        self._current_period_paid_amount = None
        self._current_period_paid_time = None
        self._damage_amount = None
        self._expanditure_publish_date = None
        self._group_id = None
        self._insurance_amount = None
        self._interest_amount = None
        self._loan_count = None
        self._penalty_interest_amount = None
        self._principal_amount = None
        self._related_loan_info = None
        self._repay_amount = None
        self._repay_bill_amount = None
        self._repay_date = None
        self._select_type = None
        self._status = None

    @property
    def allowed_pay_off_early_date(self):
        return self._allowed_pay_off_early_date

    @allowed_pay_off_early_date.setter
    def allowed_pay_off_early_date(self, value):
        self._allowed_pay_off_early_date = value
    @property
    def bill_id(self):
        return self._bill_id

    @bill_id.setter
    def bill_id(self, value):
        self._bill_id = value
    @property
    def commission_amount(self):
        return self._commission_amount

    @commission_amount.setter
    def commission_amount(self, value):
        self._commission_amount = value
    @property
    def current_period_paid_amount(self):
        return self._current_period_paid_amount

    @current_period_paid_amount.setter
    def current_period_paid_amount(self, value):
        self._current_period_paid_amount = value
    @property
    def current_period_paid_time(self):
        return self._current_period_paid_time

    @current_period_paid_time.setter
    def current_period_paid_time(self, value):
        self._current_period_paid_time = value
    @property
    def damage_amount(self):
        return self._damage_amount

    @damage_amount.setter
    def damage_amount(self, value):
        self._damage_amount = value
    @property
    def expanditure_publish_date(self):
        return self._expanditure_publish_date

    @expanditure_publish_date.setter
    def expanditure_publish_date(self, value):
        self._expanditure_publish_date = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def insurance_amount(self):
        return self._insurance_amount

    @insurance_amount.setter
    def insurance_amount(self, value):
        self._insurance_amount = value
    @property
    def interest_amount(self):
        return self._interest_amount

    @interest_amount.setter
    def interest_amount(self, value):
        self._interest_amount = value
    @property
    def loan_count(self):
        return self._loan_count

    @loan_count.setter
    def loan_count(self, value):
        self._loan_count = value
    @property
    def penalty_interest_amount(self):
        return self._penalty_interest_amount

    @penalty_interest_amount.setter
    def penalty_interest_amount(self, value):
        self._penalty_interest_amount = value
    @property
    def principal_amount(self):
        return self._principal_amount

    @principal_amount.setter
    def principal_amount(self, value):
        self._principal_amount = value
    @property
    def related_loan_info(self):
        return self._related_loan_info

    @related_loan_info.setter
    def related_loan_info(self, value):
        if isinstance(value, list):
            self._related_loan_info = list()
            for i in value:
                if isinstance(i, ConsumerLoanBillLoanRelation):
                    self._related_loan_info.append(i)
                else:
                    self._related_loan_info.append(ConsumerLoanBillLoanRelation.from_alipay_dict(i))
    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def repay_bill_amount(self):
        return self._repay_bill_amount

    @repay_bill_amount.setter
    def repay_bill_amount(self, value):
        self._repay_bill_amount = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def select_type(self):
        return self._select_type

    @select_type.setter
    def select_type(self, value):
        self._select_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.allowed_pay_off_early_date:
            if hasattr(self.allowed_pay_off_early_date, 'to_alipay_dict'):
                params['allowed_pay_off_early_date'] = self.allowed_pay_off_early_date.to_alipay_dict()
            else:
                params['allowed_pay_off_early_date'] = self.allowed_pay_off_early_date
        if self.bill_id:
            if hasattr(self.bill_id, 'to_alipay_dict'):
                params['bill_id'] = self.bill_id.to_alipay_dict()
            else:
                params['bill_id'] = self.bill_id
        if self.commission_amount:
            if hasattr(self.commission_amount, 'to_alipay_dict'):
                params['commission_amount'] = self.commission_amount.to_alipay_dict()
            else:
                params['commission_amount'] = self.commission_amount
        if self.current_period_paid_amount:
            if hasattr(self.current_period_paid_amount, 'to_alipay_dict'):
                params['current_period_paid_amount'] = self.current_period_paid_amount.to_alipay_dict()
            else:
                params['current_period_paid_amount'] = self.current_period_paid_amount
        if self.current_period_paid_time:
            if hasattr(self.current_period_paid_time, 'to_alipay_dict'):
                params['current_period_paid_time'] = self.current_period_paid_time.to_alipay_dict()
            else:
                params['current_period_paid_time'] = self.current_period_paid_time
        if self.damage_amount:
            if hasattr(self.damage_amount, 'to_alipay_dict'):
                params['damage_amount'] = self.damage_amount.to_alipay_dict()
            else:
                params['damage_amount'] = self.damage_amount
        if self.expanditure_publish_date:
            if hasattr(self.expanditure_publish_date, 'to_alipay_dict'):
                params['expanditure_publish_date'] = self.expanditure_publish_date.to_alipay_dict()
            else:
                params['expanditure_publish_date'] = self.expanditure_publish_date
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.insurance_amount:
            if hasattr(self.insurance_amount, 'to_alipay_dict'):
                params['insurance_amount'] = self.insurance_amount.to_alipay_dict()
            else:
                params['insurance_amount'] = self.insurance_amount
        if self.interest_amount:
            if hasattr(self.interest_amount, 'to_alipay_dict'):
                params['interest_amount'] = self.interest_amount.to_alipay_dict()
            else:
                params['interest_amount'] = self.interest_amount
        if self.loan_count:
            if hasattr(self.loan_count, 'to_alipay_dict'):
                params['loan_count'] = self.loan_count.to_alipay_dict()
            else:
                params['loan_count'] = self.loan_count
        if self.penalty_interest_amount:
            if hasattr(self.penalty_interest_amount, 'to_alipay_dict'):
                params['penalty_interest_amount'] = self.penalty_interest_amount.to_alipay_dict()
            else:
                params['penalty_interest_amount'] = self.penalty_interest_amount
        if self.principal_amount:
            if hasattr(self.principal_amount, 'to_alipay_dict'):
                params['principal_amount'] = self.principal_amount.to_alipay_dict()
            else:
                params['principal_amount'] = self.principal_amount
        if self.related_loan_info:
            if isinstance(self.related_loan_info, list):
                for i in range(0, len(self.related_loan_info)):
                    element = self.related_loan_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_loan_info[i] = element.to_alipay_dict()
            if hasattr(self.related_loan_info, 'to_alipay_dict'):
                params['related_loan_info'] = self.related_loan_info.to_alipay_dict()
            else:
                params['related_loan_info'] = self.related_loan_info
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.repay_bill_amount:
            if hasattr(self.repay_bill_amount, 'to_alipay_dict'):
                params['repay_bill_amount'] = self.repay_bill_amount.to_alipay_dict()
            else:
                params['repay_bill_amount'] = self.repay_bill_amount
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        if self.select_type:
            if hasattr(self.select_type, 'to_alipay_dict'):
                params['select_type'] = self.select_type.to_alipay_dict()
            else:
                params['select_type'] = self.select_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanBillInfoItem()
        if 'allowed_pay_off_early_date' in d:
            o.allowed_pay_off_early_date = d['allowed_pay_off_early_date']
        if 'bill_id' in d:
            o.bill_id = d['bill_id']
        if 'commission_amount' in d:
            o.commission_amount = d['commission_amount']
        if 'current_period_paid_amount' in d:
            o.current_period_paid_amount = d['current_period_paid_amount']
        if 'current_period_paid_time' in d:
            o.current_period_paid_time = d['current_period_paid_time']
        if 'damage_amount' in d:
            o.damage_amount = d['damage_amount']
        if 'expanditure_publish_date' in d:
            o.expanditure_publish_date = d['expanditure_publish_date']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'insurance_amount' in d:
            o.insurance_amount = d['insurance_amount']
        if 'interest_amount' in d:
            o.interest_amount = d['interest_amount']
        if 'loan_count' in d:
            o.loan_count = d['loan_count']
        if 'penalty_interest_amount' in d:
            o.penalty_interest_amount = d['penalty_interest_amount']
        if 'principal_amount' in d:
            o.principal_amount = d['principal_amount']
        if 'related_loan_info' in d:
            o.related_loan_info = d['related_loan_info']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_bill_amount' in d:
            o.repay_bill_amount = d['repay_bill_amount']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'select_type' in d:
            o.select_type = d['select_type']
        if 'status' in d:
            o.status = d['status']
        return o


