#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PenCaseInfo(object):

    def __init__(self):
        self._credit_code = None
        self._illegact_type = None
        self._open_date = None
        self._pen_auth = None
        self._pen_con = None
        self._pen_dec_no = None
        self._pendeciss_date = None
        self._unit_name = None

    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def illegact_type(self):
        return self._illegact_type

    @illegact_type.setter
    def illegact_type(self, value):
        self._illegact_type = value
    @property
    def open_date(self):
        return self._open_date

    @open_date.setter
    def open_date(self, value):
        self._open_date = value
    @property
    def pen_auth(self):
        return self._pen_auth

    @pen_auth.setter
    def pen_auth(self, value):
        self._pen_auth = value
    @property
    def pen_con(self):
        return self._pen_con

    @pen_con.setter
    def pen_con(self, value):
        self._pen_con = value
    @property
    def pen_dec_no(self):
        return self._pen_dec_no

    @pen_dec_no.setter
    def pen_dec_no(self, value):
        self._pen_dec_no = value
    @property
    def pendeciss_date(self):
        return self._pendeciss_date

    @pendeciss_date.setter
    def pendeciss_date(self, value):
        self._pendeciss_date = value
    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.illegact_type:
            if hasattr(self.illegact_type, 'to_alipay_dict'):
                params['illegact_type'] = self.illegact_type.to_alipay_dict()
            else:
                params['illegact_type'] = self.illegact_type
        if self.open_date:
            if hasattr(self.open_date, 'to_alipay_dict'):
                params['open_date'] = self.open_date.to_alipay_dict()
            else:
                params['open_date'] = self.open_date
        if self.pen_auth:
            if hasattr(self.pen_auth, 'to_alipay_dict'):
                params['pen_auth'] = self.pen_auth.to_alipay_dict()
            else:
                params['pen_auth'] = self.pen_auth
        if self.pen_con:
            if hasattr(self.pen_con, 'to_alipay_dict'):
                params['pen_con'] = self.pen_con.to_alipay_dict()
            else:
                params['pen_con'] = self.pen_con
        if self.pen_dec_no:
            if hasattr(self.pen_dec_no, 'to_alipay_dict'):
                params['pen_dec_no'] = self.pen_dec_no.to_alipay_dict()
            else:
                params['pen_dec_no'] = self.pen_dec_no
        if self.pendeciss_date:
            if hasattr(self.pendeciss_date, 'to_alipay_dict'):
                params['pendeciss_date'] = self.pendeciss_date.to_alipay_dict()
            else:
                params['pendeciss_date'] = self.pendeciss_date
        if self.unit_name:
            if hasattr(self.unit_name, 'to_alipay_dict'):
                params['unit_name'] = self.unit_name.to_alipay_dict()
            else:
                params['unit_name'] = self.unit_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PenCaseInfo()
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'illegact_type' in d:
            o.illegact_type = d['illegact_type']
        if 'open_date' in d:
            o.open_date = d['open_date']
        if 'pen_auth' in d:
            o.pen_auth = d['pen_auth']
        if 'pen_con' in d:
            o.pen_con = d['pen_con']
        if 'pen_dec_no' in d:
            o.pen_dec_no = d['pen_dec_no']
        if 'pendeciss_date' in d:
            o.pendeciss_date = d['pendeciss_date']
        if 'unit_name' in d:
            o.unit_name = d['unit_name']
        return o


