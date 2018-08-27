#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstallmentRepayPlan(object):

    def __init__(self):
        self._cur_term = None
        self._paid_int_bal = None
        self._paid_prin_bal = None
        self._status = None
        self._term_end_date = None
        self._term_no = None
        self._term_nom_int = None
        self._term_nom_prin = None
        self._term_ovd_int = None
        self._term_ovd_int_pen_int = None
        self._term_ovd_prin = None
        self._term_ovd_prin_pen_int = None
        self._term_start_date = None

    @property
    def cur_term(self):
        return self._cur_term

    @cur_term.setter
    def cur_term(self, value):
        self._cur_term = value
    @property
    def paid_int_bal(self):
        return self._paid_int_bal

    @paid_int_bal.setter
    def paid_int_bal(self, value):
        self._paid_int_bal = value
    @property
    def paid_prin_bal(self):
        return self._paid_prin_bal

    @paid_prin_bal.setter
    def paid_prin_bal(self, value):
        self._paid_prin_bal = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def term_end_date(self):
        return self._term_end_date

    @term_end_date.setter
    def term_end_date(self, value):
        self._term_end_date = value
    @property
    def term_no(self):
        return self._term_no

    @term_no.setter
    def term_no(self, value):
        self._term_no = value
    @property
    def term_nom_int(self):
        return self._term_nom_int

    @term_nom_int.setter
    def term_nom_int(self, value):
        self._term_nom_int = value
    @property
    def term_nom_prin(self):
        return self._term_nom_prin

    @term_nom_prin.setter
    def term_nom_prin(self, value):
        self._term_nom_prin = value
    @property
    def term_ovd_int(self):
        return self._term_ovd_int

    @term_ovd_int.setter
    def term_ovd_int(self, value):
        self._term_ovd_int = value
    @property
    def term_ovd_int_pen_int(self):
        return self._term_ovd_int_pen_int

    @term_ovd_int_pen_int.setter
    def term_ovd_int_pen_int(self, value):
        self._term_ovd_int_pen_int = value
    @property
    def term_ovd_prin(self):
        return self._term_ovd_prin

    @term_ovd_prin.setter
    def term_ovd_prin(self, value):
        self._term_ovd_prin = value
    @property
    def term_ovd_prin_pen_int(self):
        return self._term_ovd_prin_pen_int

    @term_ovd_prin_pen_int.setter
    def term_ovd_prin_pen_int(self, value):
        self._term_ovd_prin_pen_int = value
    @property
    def term_start_date(self):
        return self._term_start_date

    @term_start_date.setter
    def term_start_date(self, value):
        self._term_start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.cur_term:
            if hasattr(self.cur_term, 'to_alipay_dict'):
                params['cur_term'] = self.cur_term.to_alipay_dict()
            else:
                params['cur_term'] = self.cur_term
        if self.paid_int_bal:
            if hasattr(self.paid_int_bal, 'to_alipay_dict'):
                params['paid_int_bal'] = self.paid_int_bal.to_alipay_dict()
            else:
                params['paid_int_bal'] = self.paid_int_bal
        if self.paid_prin_bal:
            if hasattr(self.paid_prin_bal, 'to_alipay_dict'):
                params['paid_prin_bal'] = self.paid_prin_bal.to_alipay_dict()
            else:
                params['paid_prin_bal'] = self.paid_prin_bal
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.term_end_date:
            if hasattr(self.term_end_date, 'to_alipay_dict'):
                params['term_end_date'] = self.term_end_date.to_alipay_dict()
            else:
                params['term_end_date'] = self.term_end_date
        if self.term_no:
            if hasattr(self.term_no, 'to_alipay_dict'):
                params['term_no'] = self.term_no.to_alipay_dict()
            else:
                params['term_no'] = self.term_no
        if self.term_nom_int:
            if hasattr(self.term_nom_int, 'to_alipay_dict'):
                params['term_nom_int'] = self.term_nom_int.to_alipay_dict()
            else:
                params['term_nom_int'] = self.term_nom_int
        if self.term_nom_prin:
            if hasattr(self.term_nom_prin, 'to_alipay_dict'):
                params['term_nom_prin'] = self.term_nom_prin.to_alipay_dict()
            else:
                params['term_nom_prin'] = self.term_nom_prin
        if self.term_ovd_int:
            if hasattr(self.term_ovd_int, 'to_alipay_dict'):
                params['term_ovd_int'] = self.term_ovd_int.to_alipay_dict()
            else:
                params['term_ovd_int'] = self.term_ovd_int
        if self.term_ovd_int_pen_int:
            if hasattr(self.term_ovd_int_pen_int, 'to_alipay_dict'):
                params['term_ovd_int_pen_int'] = self.term_ovd_int_pen_int.to_alipay_dict()
            else:
                params['term_ovd_int_pen_int'] = self.term_ovd_int_pen_int
        if self.term_ovd_prin:
            if hasattr(self.term_ovd_prin, 'to_alipay_dict'):
                params['term_ovd_prin'] = self.term_ovd_prin.to_alipay_dict()
            else:
                params['term_ovd_prin'] = self.term_ovd_prin
        if self.term_ovd_prin_pen_int:
            if hasattr(self.term_ovd_prin_pen_int, 'to_alipay_dict'):
                params['term_ovd_prin_pen_int'] = self.term_ovd_prin_pen_int.to_alipay_dict()
            else:
                params['term_ovd_prin_pen_int'] = self.term_ovd_prin_pen_int
        if self.term_start_date:
            if hasattr(self.term_start_date, 'to_alipay_dict'):
                params['term_start_date'] = self.term_start_date.to_alipay_dict()
            else:
                params['term_start_date'] = self.term_start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentRepayPlan()
        if 'cur_term' in d:
            o.cur_term = d['cur_term']
        if 'paid_int_bal' in d:
            o.paid_int_bal = d['paid_int_bal']
        if 'paid_prin_bal' in d:
            o.paid_prin_bal = d['paid_prin_bal']
        if 'status' in d:
            o.status = d['status']
        if 'term_end_date' in d:
            o.term_end_date = d['term_end_date']
        if 'term_no' in d:
            o.term_no = d['term_no']
        if 'term_nom_int' in d:
            o.term_nom_int = d['term_nom_int']
        if 'term_nom_prin' in d:
            o.term_nom_prin = d['term_nom_prin']
        if 'term_ovd_int' in d:
            o.term_ovd_int = d['term_ovd_int']
        if 'term_ovd_int_pen_int' in d:
            o.term_ovd_int_pen_int = d['term_ovd_int_pen_int']
        if 'term_ovd_prin' in d:
            o.term_ovd_prin = d['term_ovd_prin']
        if 'term_ovd_prin_pen_int' in d:
            o.term_ovd_prin_pen_int = d['term_ovd_prin_pen_int']
        if 'term_start_date' in d:
            o.term_start_date = d['term_start_date']
        return o


