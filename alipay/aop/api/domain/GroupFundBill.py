#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupFundDetail import GroupFundDetail


class GroupFundBill(object):

    def __init__(self):
        self._actual_amount = None
        self._amount = None
        self._bill_no = None
        self._bill_type = None
        self._fund_details = None
        self._status = None
        self._transfer_no = None
        self._user_id = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def fund_details(self):
        return self._fund_details

    @fund_details.setter
    def fund_details(self, value):
        if isinstance(value, list):
            self._fund_details = list()
            for i in value:
                if isinstance(i, GroupFundDetail):
                    self._fund_details.append(i)
                else:
                    self._fund_details.append(GroupFundDetail.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def transfer_no(self):
        return self._transfer_no

    @transfer_no.setter
    def transfer_no(self, value):
        self._transfer_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.fund_details:
            if isinstance(self.fund_details, list):
                for i in range(0, len(self.fund_details)):
                    element = self.fund_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_details[i] = element.to_alipay_dict()
            if hasattr(self.fund_details, 'to_alipay_dict'):
                params['fund_details'] = self.fund_details.to_alipay_dict()
            else:
                params['fund_details'] = self.fund_details
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.transfer_no:
            if hasattr(self.transfer_no, 'to_alipay_dict'):
                params['transfer_no'] = self.transfer_no.to_alipay_dict()
            else:
                params['transfer_no'] = self.transfer_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupFundBill()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'fund_details' in d:
            o.fund_details = d['fund_details']
        if 'status' in d:
            o.status = d['status']
        if 'transfer_no' in d:
            o.transfer_no = d['transfer_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


