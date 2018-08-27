#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArrangementOpenQueryResultVO(object):

    def __init__(self):
        self._ar_no = None
        self._ar_status = None
        self._ext_data = None
        self._invalid_date = None
        self._sign_date = None
        self._valid_date = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def ar_status(self):
        return self._ar_status

    @ar_status.setter
    def ar_status(self, value):
        self._ar_status = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def invalid_date(self):
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = value
    @property
    def sign_date(self):
        return self._sign_date

    @sign_date.setter
    def sign_date(self, value):
        self._sign_date = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.ar_status:
            if hasattr(self.ar_status, 'to_alipay_dict'):
                params['ar_status'] = self.ar_status.to_alipay_dict()
            else:
                params['ar_status'] = self.ar_status
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.invalid_date:
            if hasattr(self.invalid_date, 'to_alipay_dict'):
                params['invalid_date'] = self.invalid_date.to_alipay_dict()
            else:
                params['invalid_date'] = self.invalid_date
        if self.sign_date:
            if hasattr(self.sign_date, 'to_alipay_dict'):
                params['sign_date'] = self.sign_date.to_alipay_dict()
            else:
                params['sign_date'] = self.sign_date
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
        o = ArrangementOpenQueryResultVO()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'ar_status' in d:
            o.ar_status = d['ar_status']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'invalid_date' in d:
            o.invalid_date = d['invalid_date']
        if 'sign_date' in d:
            o.sign_date = d['sign_date']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


