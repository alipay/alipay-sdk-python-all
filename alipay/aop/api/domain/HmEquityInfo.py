#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HmEquityInfo(object):

    def __init__(self):
        self._activated = None
        self._equity_code = None
        self._equity_name = None
        self._equity_type = None
        self._residue_quota = None
        self._total_quota = None
        self._valid_date = None

    @property
    def activated(self):
        return self._activated

    @activated.setter
    def activated(self, value):
        self._activated = value
    @property
    def equity_code(self):
        return self._equity_code

    @equity_code.setter
    def equity_code(self, value):
        self._equity_code = value
    @property
    def equity_name(self):
        return self._equity_name

    @equity_name.setter
    def equity_name(self, value):
        self._equity_name = value
    @property
    def equity_type(self):
        return self._equity_type

    @equity_type.setter
    def equity_type(self, value):
        self._equity_type = value
    @property
    def residue_quota(self):
        return self._residue_quota

    @residue_quota.setter
    def residue_quota(self, value):
        self._residue_quota = value
    @property
    def total_quota(self):
        return self._total_quota

    @total_quota.setter
    def total_quota(self, value):
        self._total_quota = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.activated:
            if hasattr(self.activated, 'to_alipay_dict'):
                params['activated'] = self.activated.to_alipay_dict()
            else:
                params['activated'] = self.activated
        if self.equity_code:
            if hasattr(self.equity_code, 'to_alipay_dict'):
                params['equity_code'] = self.equity_code.to_alipay_dict()
            else:
                params['equity_code'] = self.equity_code
        if self.equity_name:
            if hasattr(self.equity_name, 'to_alipay_dict'):
                params['equity_name'] = self.equity_name.to_alipay_dict()
            else:
                params['equity_name'] = self.equity_name
        if self.equity_type:
            if hasattr(self.equity_type, 'to_alipay_dict'):
                params['equity_type'] = self.equity_type.to_alipay_dict()
            else:
                params['equity_type'] = self.equity_type
        if self.residue_quota:
            if hasattr(self.residue_quota, 'to_alipay_dict'):
                params['residue_quota'] = self.residue_quota.to_alipay_dict()
            else:
                params['residue_quota'] = self.residue_quota
        if self.total_quota:
            if hasattr(self.total_quota, 'to_alipay_dict'):
                params['total_quota'] = self.total_quota.to_alipay_dict()
            else:
                params['total_quota'] = self.total_quota
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
        o = HmEquityInfo()
        if 'activated' in d:
            o.activated = d['activated']
        if 'equity_code' in d:
            o.equity_code = d['equity_code']
        if 'equity_name' in d:
            o.equity_name = d['equity_name']
        if 'equity_type' in d:
            o.equity_type = d['equity_type']
        if 'residue_quota' in d:
            o.residue_quota = d['residue_quota']
        if 'total_quota' in d:
            o.total_quota = d['total_quota']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


