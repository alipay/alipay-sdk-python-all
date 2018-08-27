#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CodeNOList(object):

    def __init__(self):
        self._amount = None
        self._code_no = None
        self._sub_type = None
        self._ticket_type = None
        self._valid_date = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def code_no(self):
        return self._code_no

    @code_no.setter
    def code_no(self, value):
        self._code_no = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.code_no:
            if hasattr(self.code_no, 'to_alipay_dict'):
                params['code_no'] = self.code_no.to_alipay_dict()
            else:
                params['code_no'] = self.code_no
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.ticket_type:
            if hasattr(self.ticket_type, 'to_alipay_dict'):
                params['ticket_type'] = self.ticket_type.to_alipay_dict()
            else:
                params['ticket_type'] = self.ticket_type
        if self.valid_date:
            if hasattr(self.valid_date, 'to_alipay_dict'):
                params['valid_date'] = self.valid_date.to_alipay_dict()
            else:
                params['valid_date'] = self.valid_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CodeNOList()
        if 'amount' in d:
            o.amount = d['amount']
        if 'code_no' in d:
            o.code_no = d['code_no']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


