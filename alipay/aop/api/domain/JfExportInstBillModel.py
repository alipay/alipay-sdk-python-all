#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JfExportInstBillModel(object):

    def __init__(self):
        self._amount = None
        self._balance = None
        self._bill_date = None
        self._bill_fines = None
        self._bill_key = None
        self._extend_field = None
        self._inst_bill_no = None
        self._owner_name = None
        self._uniq_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_fines(self):
        return self._bill_fines

    @bill_fines.setter
    def bill_fines(self, value):
        self._bill_fines = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def inst_bill_no(self):
        return self._inst_bill_no

    @inst_bill_no.setter
    def inst_bill_no(self, value):
        self._inst_bill_no = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def uniq_id(self):
        return self._uniq_id

    @uniq_id.setter
    def uniq_id(self, value):
        self._uniq_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_fines:
            if hasattr(self.bill_fines, 'to_alipay_dict'):
                params['bill_fines'] = self.bill_fines.to_alipay_dict()
            else:
                params['bill_fines'] = self.bill_fines
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.inst_bill_no:
            if hasattr(self.inst_bill_no, 'to_alipay_dict'):
                params['inst_bill_no'] = self.inst_bill_no.to_alipay_dict()
            else:
                params['inst_bill_no'] = self.inst_bill_no
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.uniq_id:
            if hasattr(self.uniq_id, 'to_alipay_dict'):
                params['uniq_id'] = self.uniq_id.to_alipay_dict()
            else:
                params['uniq_id'] = self.uniq_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JfExportInstBillModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'balance' in d:
            o.balance = d['balance']
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_fines' in d:
            o.bill_fines = d['bill_fines']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'inst_bill_no' in d:
            o.inst_bill_no = d['inst_bill_no']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'uniq_id' in d:
            o.uniq_id = d['uniq_id']
        return o


