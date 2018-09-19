#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneProdBillDetail(object):

    def __init__(self):
        self._bill_type = None
        self._due_date = None
        self._int_amt = None
        self._overdue_days = None
        self._pen_amt = None
        self._prin_amt = None
        self._remark = None
        self._status = None
        self._term = None
        self._total_amt = None

    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def int_amt(self):
        return self._int_amt

    @int_amt.setter
    def int_amt(self, value):
        self._int_amt = value
    @property
    def overdue_days(self):
        return self._overdue_days

    @overdue_days.setter
    def overdue_days(self, value):
        self._overdue_days = value
    @property
    def pen_amt(self):
        return self._pen_amt

    @pen_amt.setter
    def pen_amt(self, value):
        self._pen_amt = value
    @property
    def prin_amt(self):
        return self._prin_amt

    @prin_amt.setter
    def prin_amt(self, value):
        self._prin_amt = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        self._total_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.due_date:
            if hasattr(self.due_date, 'to_alipay_dict'):
                params['due_date'] = self.due_date.to_alipay_dict()
            else:
                params['due_date'] = self.due_date
        if self.int_amt:
            if hasattr(self.int_amt, 'to_alipay_dict'):
                params['int_amt'] = self.int_amt.to_alipay_dict()
            else:
                params['int_amt'] = self.int_amt
        if self.overdue_days:
            if hasattr(self.overdue_days, 'to_alipay_dict'):
                params['overdue_days'] = self.overdue_days.to_alipay_dict()
            else:
                params['overdue_days'] = self.overdue_days
        if self.pen_amt:
            if hasattr(self.pen_amt, 'to_alipay_dict'):
                params['pen_amt'] = self.pen_amt.to_alipay_dict()
            else:
                params['pen_amt'] = self.pen_amt
        if self.prin_amt:
            if hasattr(self.prin_amt, 'to_alipay_dict'):
                params['prin_amt'] = self.prin_amt.to_alipay_dict()
            else:
                params['prin_amt'] = self.prin_amt
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.term:
            if hasattr(self.term, 'to_alipay_dict'):
                params['term'] = self.term.to_alipay_dict()
            else:
                params['term'] = self.term
        if self.total_amt:
            if hasattr(self.total_amt, 'to_alipay_dict'):
                params['total_amt'] = self.total_amt.to_alipay_dict()
            else:
                params['total_amt'] = self.total_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneProdBillDetail()
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'due_date' in d:
            o.due_date = d['due_date']
        if 'int_amt' in d:
            o.int_amt = d['int_amt']
        if 'overdue_days' in d:
            o.overdue_days = d['overdue_days']
        if 'pen_amt' in d:
            o.pen_amt = d['pen_amt']
        if 'prin_amt' in d:
            o.prin_amt = d['prin_amt']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        if 'term' in d:
            o.term = d['term']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        return o


