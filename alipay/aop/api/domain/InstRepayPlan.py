#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstRepayPlan(object):

    def __init__(self):
        self._cur_term = None
        self._cur_term_interest = None
        self._cur_term_interest_penalty = None
        self._cur_term_principal = None
        self._cur_term_principal_penalty = None
        self._repaid_interest = None
        self._repaid_interest_penalty = None
        self._repaid_principal = None
        self._repaid_principal_penalty = None
        self._status = None
        self._term_end_date = None
        self._term_no = None
        self._term_start_date = None

    @property
    def cur_term(self):
        return self._cur_term

    @cur_term.setter
    def cur_term(self, value):
        self._cur_term = value
    @property
    def cur_term_interest(self):
        return self._cur_term_interest

    @cur_term_interest.setter
    def cur_term_interest(self, value):
        self._cur_term_interest = value
    @property
    def cur_term_interest_penalty(self):
        return self._cur_term_interest_penalty

    @cur_term_interest_penalty.setter
    def cur_term_interest_penalty(self, value):
        self._cur_term_interest_penalty = value
    @property
    def cur_term_principal(self):
        return self._cur_term_principal

    @cur_term_principal.setter
    def cur_term_principal(self, value):
        self._cur_term_principal = value
    @property
    def cur_term_principal_penalty(self):
        return self._cur_term_principal_penalty

    @cur_term_principal_penalty.setter
    def cur_term_principal_penalty(self, value):
        self._cur_term_principal_penalty = value
    @property
    def repaid_interest(self):
        return self._repaid_interest

    @repaid_interest.setter
    def repaid_interest(self, value):
        self._repaid_interest = value
    @property
    def repaid_interest_penalty(self):
        return self._repaid_interest_penalty

    @repaid_interest_penalty.setter
    def repaid_interest_penalty(self, value):
        self._repaid_interest_penalty = value
    @property
    def repaid_principal(self):
        return self._repaid_principal

    @repaid_principal.setter
    def repaid_principal(self, value):
        self._repaid_principal = value
    @property
    def repaid_principal_penalty(self):
        return self._repaid_principal_penalty

    @repaid_principal_penalty.setter
    def repaid_principal_penalty(self, value):
        self._repaid_principal_penalty = value
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
        if self.cur_term_interest:
            if hasattr(self.cur_term_interest, 'to_alipay_dict'):
                params['cur_term_interest'] = self.cur_term_interest.to_alipay_dict()
            else:
                params['cur_term_interest'] = self.cur_term_interest
        if self.cur_term_interest_penalty:
            if hasattr(self.cur_term_interest_penalty, 'to_alipay_dict'):
                params['cur_term_interest_penalty'] = self.cur_term_interest_penalty.to_alipay_dict()
            else:
                params['cur_term_interest_penalty'] = self.cur_term_interest_penalty
        if self.cur_term_principal:
            if hasattr(self.cur_term_principal, 'to_alipay_dict'):
                params['cur_term_principal'] = self.cur_term_principal.to_alipay_dict()
            else:
                params['cur_term_principal'] = self.cur_term_principal
        if self.cur_term_principal_penalty:
            if hasattr(self.cur_term_principal_penalty, 'to_alipay_dict'):
                params['cur_term_principal_penalty'] = self.cur_term_principal_penalty.to_alipay_dict()
            else:
                params['cur_term_principal_penalty'] = self.cur_term_principal_penalty
        if self.repaid_interest:
            if hasattr(self.repaid_interest, 'to_alipay_dict'):
                params['repaid_interest'] = self.repaid_interest.to_alipay_dict()
            else:
                params['repaid_interest'] = self.repaid_interest
        if self.repaid_interest_penalty:
            if hasattr(self.repaid_interest_penalty, 'to_alipay_dict'):
                params['repaid_interest_penalty'] = self.repaid_interest_penalty.to_alipay_dict()
            else:
                params['repaid_interest_penalty'] = self.repaid_interest_penalty
        if self.repaid_principal:
            if hasattr(self.repaid_principal, 'to_alipay_dict'):
                params['repaid_principal'] = self.repaid_principal.to_alipay_dict()
            else:
                params['repaid_principal'] = self.repaid_principal
        if self.repaid_principal_penalty:
            if hasattr(self.repaid_principal_penalty, 'to_alipay_dict'):
                params['repaid_principal_penalty'] = self.repaid_principal_penalty.to_alipay_dict()
            else:
                params['repaid_principal_penalty'] = self.repaid_principal_penalty
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
        o = InstRepayPlan()
        if 'cur_term' in d:
            o.cur_term = d['cur_term']
        if 'cur_term_interest' in d:
            o.cur_term_interest = d['cur_term_interest']
        if 'cur_term_interest_penalty' in d:
            o.cur_term_interest_penalty = d['cur_term_interest_penalty']
        if 'cur_term_principal' in d:
            o.cur_term_principal = d['cur_term_principal']
        if 'cur_term_principal_penalty' in d:
            o.cur_term_principal_penalty = d['cur_term_principal_penalty']
        if 'repaid_interest' in d:
            o.repaid_interest = d['repaid_interest']
        if 'repaid_interest_penalty' in d:
            o.repaid_interest_penalty = d['repaid_interest_penalty']
        if 'repaid_principal' in d:
            o.repaid_principal = d['repaid_principal']
        if 'repaid_principal_penalty' in d:
            o.repaid_principal_penalty = d['repaid_principal_penalty']
        if 'status' in d:
            o.status = d['status']
        if 'term_end_date' in d:
            o.term_end_date = d['term_end_date']
        if 'term_no' in d:
            o.term_no = d['term_no']
        if 'term_start_date' in d:
            o.term_start_date = d['term_start_date']
        return o


