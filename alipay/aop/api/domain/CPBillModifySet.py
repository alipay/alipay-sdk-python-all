#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CPBillModifySet(object):

    def __init__(self):
        self._acct_period = None
        self._bill_entry_amount = None
        self._bill_entry_id = None
        self._cost_type = None
        self._deadline = None
        self._release_day = None
        self._room_address = None

    @property
    def acct_period(self):
        return self._acct_period

    @acct_period.setter
    def acct_period(self, value):
        self._acct_period = value
    @property
    def bill_entry_amount(self):
        return self._bill_entry_amount

    @bill_entry_amount.setter
    def bill_entry_amount(self, value):
        self._bill_entry_amount = value
    @property
    def bill_entry_id(self):
        return self._bill_entry_id

    @bill_entry_id.setter
    def bill_entry_id(self, value):
        self._bill_entry_id = value
    @property
    def cost_type(self):
        return self._cost_type

    @cost_type.setter
    def cost_type(self, value):
        self._cost_type = value
    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value
    @property
    def release_day(self):
        return self._release_day

    @release_day.setter
    def release_day(self, value):
        self._release_day = value
    @property
    def room_address(self):
        return self._room_address

    @room_address.setter
    def room_address(self, value):
        self._room_address = value


    def to_alipay_dict(self):
        params = dict()
        if self.acct_period:
            if hasattr(self.acct_period, 'to_alipay_dict'):
                params['acct_period'] = self.acct_period.to_alipay_dict()
            else:
                params['acct_period'] = self.acct_period
        if self.bill_entry_amount:
            if hasattr(self.bill_entry_amount, 'to_alipay_dict'):
                params['bill_entry_amount'] = self.bill_entry_amount.to_alipay_dict()
            else:
                params['bill_entry_amount'] = self.bill_entry_amount
        if self.bill_entry_id:
            if hasattr(self.bill_entry_id, 'to_alipay_dict'):
                params['bill_entry_id'] = self.bill_entry_id.to_alipay_dict()
            else:
                params['bill_entry_id'] = self.bill_entry_id
        if self.cost_type:
            if hasattr(self.cost_type, 'to_alipay_dict'):
                params['cost_type'] = self.cost_type.to_alipay_dict()
            else:
                params['cost_type'] = self.cost_type
        if self.deadline:
            if hasattr(self.deadline, 'to_alipay_dict'):
                params['deadline'] = self.deadline.to_alipay_dict()
            else:
                params['deadline'] = self.deadline
        if self.release_day:
            if hasattr(self.release_day, 'to_alipay_dict'):
                params['release_day'] = self.release_day.to_alipay_dict()
            else:
                params['release_day'] = self.release_day
        if self.room_address:
            if hasattr(self.room_address, 'to_alipay_dict'):
                params['room_address'] = self.room_address.to_alipay_dict()
            else:
                params['room_address'] = self.room_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CPBillModifySet()
        if 'acct_period' in d:
            o.acct_period = d['acct_period']
        if 'bill_entry_amount' in d:
            o.bill_entry_amount = d['bill_entry_amount']
        if 'bill_entry_id' in d:
            o.bill_entry_id = d['bill_entry_id']
        if 'cost_type' in d:
            o.cost_type = d['cost_type']
        if 'deadline' in d:
            o.deadline = d['deadline']
        if 'release_day' in d:
            o.release_day = d['release_day']
        if 'room_address' in d:
            o.room_address = d['room_address']
        return o


