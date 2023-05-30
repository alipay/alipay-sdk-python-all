#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthEcsignSealAuthModel(object):

    def __init__(self):
        self._auth_alipay_no = None
        self._auth_end_date = None
        self._auth_start_date = None
        self._seal_id = None

    @property
    def auth_alipay_no(self):
        return self._auth_alipay_no

    @auth_alipay_no.setter
    def auth_alipay_no(self, value):
        self._auth_alipay_no = value
    @property
    def auth_end_date(self):
        return self._auth_end_date

    @auth_end_date.setter
    def auth_end_date(self, value):
        self._auth_end_date = value
    @property
    def auth_start_date(self):
        return self._auth_start_date

    @auth_start_date.setter
    def auth_start_date(self, value):
        self._auth_start_date = value
    @property
    def seal_id(self):
        return self._seal_id

    @seal_id.setter
    def seal_id(self, value):
        self._seal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_alipay_no:
            if hasattr(self.auth_alipay_no, 'to_alipay_dict'):
                params['auth_alipay_no'] = self.auth_alipay_no.to_alipay_dict()
            else:
                params['auth_alipay_no'] = self.auth_alipay_no
        if self.auth_end_date:
            if hasattr(self.auth_end_date, 'to_alipay_dict'):
                params['auth_end_date'] = self.auth_end_date.to_alipay_dict()
            else:
                params['auth_end_date'] = self.auth_end_date
        if self.auth_start_date:
            if hasattr(self.auth_start_date, 'to_alipay_dict'):
                params['auth_start_date'] = self.auth_start_date.to_alipay_dict()
            else:
                params['auth_start_date'] = self.auth_start_date
        if self.seal_id:
            if hasattr(self.seal_id, 'to_alipay_dict'):
                params['seal_id'] = self.seal_id.to_alipay_dict()
            else:
                params['seal_id'] = self.seal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthEcsignSealAuthModel()
        if 'auth_alipay_no' in d:
            o.auth_alipay_no = d['auth_alipay_no']
        if 'auth_end_date' in d:
            o.auth_end_date = d['auth_end_date']
        if 'auth_start_date' in d:
            o.auth_start_date = d['auth_start_date']
        if 'seal_id' in d:
            o.seal_id = d['seal_id']
        return o


