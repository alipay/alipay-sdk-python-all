#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseBill(object):

    def __init__(self):
        self._bill_amount = None
        self._bill_create_time = None
        self._bill_desc = None
        self._bill_no = None
        self._bill_status = None
        self._bill_type = None
        self._deadline_date = None
        self._deduction_amount = None
        self._discount_amount = None
        self._end_date = None
        self._lease_no = None
        self._memo = None
        self._min_pay_amount = None
        self._paid_amount = None
        self._pay_lock = None
        self._pay_lock_memo = None
        self._pay_status = None
        self._pay_time = None
        self._start_date = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_create_time(self):
        return self._bill_create_time

    @bill_create_time.setter
    def bill_create_time(self, value):
        self._bill_create_time = value
    @property
    def bill_desc(self):
        return self._bill_desc

    @bill_desc.setter
    def bill_desc(self, value):
        self._bill_desc = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def deadline_date(self):
        return self._deadline_date

    @deadline_date.setter
    def deadline_date(self, value):
        self._deadline_date = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def lease_no(self):
        return self._lease_no

    @lease_no.setter
    def lease_no(self, value):
        self._lease_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def min_pay_amount(self):
        return self._min_pay_amount

    @min_pay_amount.setter
    def min_pay_amount(self, value):
        self._min_pay_amount = value
    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self._paid_amount = value
    @property
    def pay_lock(self):
        return self._pay_lock

    @pay_lock.setter
    def pay_lock(self, value):
        self._pay_lock = value
    @property
    def pay_lock_memo(self):
        return self._pay_lock_memo

    @pay_lock_memo.setter
    def pay_lock_memo(self, value):
        self._pay_lock_memo = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_create_time:
            if hasattr(self.bill_create_time, 'to_alipay_dict'):
                params['bill_create_time'] = self.bill_create_time.to_alipay_dict()
            else:
                params['bill_create_time'] = self.bill_create_time
        if self.bill_desc:
            if hasattr(self.bill_desc, 'to_alipay_dict'):
                params['bill_desc'] = self.bill_desc.to_alipay_dict()
            else:
                params['bill_desc'] = self.bill_desc
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.deadline_date:
            if hasattr(self.deadline_date, 'to_alipay_dict'):
                params['deadline_date'] = self.deadline_date.to_alipay_dict()
            else:
                params['deadline_date'] = self.deadline_date
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.lease_no:
            if hasattr(self.lease_no, 'to_alipay_dict'):
                params['lease_no'] = self.lease_no.to_alipay_dict()
            else:
                params['lease_no'] = self.lease_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.min_pay_amount:
            if hasattr(self.min_pay_amount, 'to_alipay_dict'):
                params['min_pay_amount'] = self.min_pay_amount.to_alipay_dict()
            else:
                params['min_pay_amount'] = self.min_pay_amount
        if self.paid_amount:
            if hasattr(self.paid_amount, 'to_alipay_dict'):
                params['paid_amount'] = self.paid_amount.to_alipay_dict()
            else:
                params['paid_amount'] = self.paid_amount
        if self.pay_lock:
            if hasattr(self.pay_lock, 'to_alipay_dict'):
                params['pay_lock'] = self.pay_lock.to_alipay_dict()
            else:
                params['pay_lock'] = self.pay_lock
        if self.pay_lock_memo:
            if hasattr(self.pay_lock_memo, 'to_alipay_dict'):
                params['pay_lock_memo'] = self.pay_lock_memo.to_alipay_dict()
            else:
                params['pay_lock_memo'] = self.pay_lock_memo
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseBill()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_create_time' in d:
            o.bill_create_time = d['bill_create_time']
        if 'bill_desc' in d:
            o.bill_desc = d['bill_desc']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'deadline_date' in d:
            o.deadline_date = d['deadline_date']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'lease_no' in d:
            o.lease_no = d['lease_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'min_pay_amount' in d:
            o.min_pay_amount = d['min_pay_amount']
        if 'paid_amount' in d:
            o.paid_amount = d['paid_amount']
        if 'pay_lock' in d:
            o.pay_lock = d['pay_lock']
        if 'pay_lock_memo' in d:
            o.pay_lock_memo = d['pay_lock_memo']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


