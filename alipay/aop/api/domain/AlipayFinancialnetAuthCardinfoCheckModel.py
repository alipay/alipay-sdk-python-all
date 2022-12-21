#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthCardinfoCheckModel(object):

    def __init__(self):
        self._card_bin_check = None
        self._card_no = None
        self._cvv_2 = None
        self._do_update = None
        self._valid_date = None

    @property
    def card_bin_check(self):
        return self._card_bin_check

    @card_bin_check.setter
    def card_bin_check(self, value):
        self._card_bin_check = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def cvv_2(self):
        return self._cvv_2

    @cvv_2.setter
    def cvv_2(self, value):
        self._cvv_2 = value
    @property
    def do_update(self):
        return self._do_update

    @do_update.setter
    def do_update(self, value):
        self._do_update = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_bin_check:
            if hasattr(self.card_bin_check, 'to_alipay_dict'):
                params['card_bin_check'] = self.card_bin_check.to_alipay_dict()
            else:
                params['card_bin_check'] = self.card_bin_check
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.cvv_2:
            if hasattr(self.cvv_2, 'to_alipay_dict'):
                params['cvv_2'] = self.cvv_2.to_alipay_dict()
            else:
                params['cvv_2'] = self.cvv_2
        if self.do_update:
            if hasattr(self.do_update, 'to_alipay_dict'):
                params['do_update'] = self.do_update.to_alipay_dict()
            else:
                params['do_update'] = self.do_update
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
        o = AlipayFinancialnetAuthCardinfoCheckModel()
        if 'card_bin_check' in d:
            o.card_bin_check = d['card_bin_check']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'cvv_2' in d:
            o.cvv_2 = d['cvv_2']
        if 'do_update' in d:
            o.do_update = d['do_update']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


