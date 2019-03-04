#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneProdBillDetail(object):

    def __init__(self):
        self._bill_type = None
        self._clear_date = None
        self._currency = None
        self._discount_amt = None
        self._due_date = None
        self._int_amt = None
        self._other_amt = None
        self._overdue_days = None
        self._paid_int_amt = None
        self._paid_other_amt = None
        self._paid_pen_amt = None
        self._paid_prin_amt = None
        self._paid_total_amt = None
        self._pen_amt = None
        self._prin_amt = None
        self._real_repay_date = None
        self._remark = None
        self._status = None
        self._term = None
        self._term_end_date = None
        self._term_start_date = None
        self._total_amt = None

    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def clear_date(self):
        return self._clear_date

    @clear_date.setter
    def clear_date(self, value):
        self._clear_date = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def discount_amt(self):
        return self._discount_amt

    @discount_amt.setter
    def discount_amt(self, value):
        self._discount_amt = value
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
    def other_amt(self):
        return self._other_amt

    @other_amt.setter
    def other_amt(self, value):
        self._other_amt = value
    @property
    def overdue_days(self):
        return self._overdue_days

    @overdue_days.setter
    def overdue_days(self, value):
        self._overdue_days = value
    @property
    def paid_int_amt(self):
        return self._paid_int_amt

    @paid_int_amt.setter
    def paid_int_amt(self, value):
        self._paid_int_amt = value
    @property
    def paid_other_amt(self):
        return self._paid_other_amt

    @paid_other_amt.setter
    def paid_other_amt(self, value):
        self._paid_other_amt = value
    @property
    def paid_pen_amt(self):
        return self._paid_pen_amt

    @paid_pen_amt.setter
    def paid_pen_amt(self, value):
        self._paid_pen_amt = value
    @property
    def paid_prin_amt(self):
        return self._paid_prin_amt

    @paid_prin_amt.setter
    def paid_prin_amt(self, value):
        self._paid_prin_amt = value
    @property
    def paid_total_amt(self):
        return self._paid_total_amt

    @paid_total_amt.setter
    def paid_total_amt(self, value):
        self._paid_total_amt = value
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
    def real_repay_date(self):
        return self._real_repay_date

    @real_repay_date.setter
    def real_repay_date(self, value):
        self._real_repay_date = value
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
    def term_end_date(self):
        return self._term_end_date

    @term_end_date.setter
    def term_end_date(self, value):
        self._term_end_date = value
    @property
    def term_start_date(self):
        return self._term_start_date

    @term_start_date.setter
    def term_start_date(self, value):
        self._term_start_date = value
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
        if self.clear_date:
            if hasattr(self.clear_date, 'to_alipay_dict'):
                params['clear_date'] = self.clear_date.to_alipay_dict()
            else:
                params['clear_date'] = self.clear_date
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.discount_amt:
            if hasattr(self.discount_amt, 'to_alipay_dict'):
                params['discount_amt'] = self.discount_amt.to_alipay_dict()
            else:
                params['discount_amt'] = self.discount_amt
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
        if self.other_amt:
            if hasattr(self.other_amt, 'to_alipay_dict'):
                params['other_amt'] = self.other_amt.to_alipay_dict()
            else:
                params['other_amt'] = self.other_amt
        if self.overdue_days:
            if hasattr(self.overdue_days, 'to_alipay_dict'):
                params['overdue_days'] = self.overdue_days.to_alipay_dict()
            else:
                params['overdue_days'] = self.overdue_days
        if self.paid_int_amt:
            if hasattr(self.paid_int_amt, 'to_alipay_dict'):
                params['paid_int_amt'] = self.paid_int_amt.to_alipay_dict()
            else:
                params['paid_int_amt'] = self.paid_int_amt
        if self.paid_other_amt:
            if hasattr(self.paid_other_amt, 'to_alipay_dict'):
                params['paid_other_amt'] = self.paid_other_amt.to_alipay_dict()
            else:
                params['paid_other_amt'] = self.paid_other_amt
        if self.paid_pen_amt:
            if hasattr(self.paid_pen_amt, 'to_alipay_dict'):
                params['paid_pen_amt'] = self.paid_pen_amt.to_alipay_dict()
            else:
                params['paid_pen_amt'] = self.paid_pen_amt
        if self.paid_prin_amt:
            if hasattr(self.paid_prin_amt, 'to_alipay_dict'):
                params['paid_prin_amt'] = self.paid_prin_amt.to_alipay_dict()
            else:
                params['paid_prin_amt'] = self.paid_prin_amt
        if self.paid_total_amt:
            if hasattr(self.paid_total_amt, 'to_alipay_dict'):
                params['paid_total_amt'] = self.paid_total_amt.to_alipay_dict()
            else:
                params['paid_total_amt'] = self.paid_total_amt
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
        if self.real_repay_date:
            if hasattr(self.real_repay_date, 'to_alipay_dict'):
                params['real_repay_date'] = self.real_repay_date.to_alipay_dict()
            else:
                params['real_repay_date'] = self.real_repay_date
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
        if self.term_end_date:
            if hasattr(self.term_end_date, 'to_alipay_dict'):
                params['term_end_date'] = self.term_end_date.to_alipay_dict()
            else:
                params['term_end_date'] = self.term_end_date
        if self.term_start_date:
            if hasattr(self.term_start_date, 'to_alipay_dict'):
                params['term_start_date'] = self.term_start_date.to_alipay_dict()
            else:
                params['term_start_date'] = self.term_start_date
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
        if 'clear_date' in d:
            o.clear_date = d['clear_date']
        if 'currency' in d:
            o.currency = d['currency']
        if 'discount_amt' in d:
            o.discount_amt = d['discount_amt']
        if 'due_date' in d:
            o.due_date = d['due_date']
        if 'int_amt' in d:
            o.int_amt = d['int_amt']
        if 'other_amt' in d:
            o.other_amt = d['other_amt']
        if 'overdue_days' in d:
            o.overdue_days = d['overdue_days']
        if 'paid_int_amt' in d:
            o.paid_int_amt = d['paid_int_amt']
        if 'paid_other_amt' in d:
            o.paid_other_amt = d['paid_other_amt']
        if 'paid_pen_amt' in d:
            o.paid_pen_amt = d['paid_pen_amt']
        if 'paid_prin_amt' in d:
            o.paid_prin_amt = d['paid_prin_amt']
        if 'paid_total_amt' in d:
            o.paid_total_amt = d['paid_total_amt']
        if 'pen_amt' in d:
            o.pen_amt = d['pen_amt']
        if 'prin_amt' in d:
            o.prin_amt = d['prin_amt']
        if 'real_repay_date' in d:
            o.real_repay_date = d['real_repay_date']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        if 'term' in d:
            o.term = d['term']
        if 'term_end_date' in d:
            o.term_end_date = d['term_end_date']
        if 'term_start_date' in d:
            o.term_start_date = d['term_start_date']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        return o


