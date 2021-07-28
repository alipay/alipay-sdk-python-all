#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubAccountBaseInfo(object):

    def __init__(self):
        self._account_no = None
        self._out_fin_inst_abbreviation = None
        self._sub_account_no = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def out_fin_inst_abbreviation(self):
        return self._out_fin_inst_abbreviation

    @out_fin_inst_abbreviation.setter
    def out_fin_inst_abbreviation(self, value):
        self._out_fin_inst_abbreviation = value
    @property
    def sub_account_no(self):
        return self._sub_account_no

    @sub_account_no.setter
    def sub_account_no(self, value):
        self._sub_account_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.out_fin_inst_abbreviation:
            if hasattr(self.out_fin_inst_abbreviation, 'to_alipay_dict'):
                params['out_fin_inst_abbreviation'] = self.out_fin_inst_abbreviation.to_alipay_dict()
            else:
                params['out_fin_inst_abbreviation'] = self.out_fin_inst_abbreviation
        if self.sub_account_no:
            if hasattr(self.sub_account_no, 'to_alipay_dict'):
                params['sub_account_no'] = self.sub_account_no.to_alipay_dict()
            else:
                params['sub_account_no'] = self.sub_account_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountBaseInfo()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'out_fin_inst_abbreviation' in d:
            o.out_fin_inst_abbreviation = d['out_fin_inst_abbreviation']
        if 'sub_account_no' in d:
            o.sub_account_no = d['sub_account_no']
        return o


