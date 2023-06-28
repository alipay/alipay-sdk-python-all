#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceIncomeStatementVerifyModel(object):

    def __init__(self):
        self._biz_no = None
        self._distribution_pro_no = None
        self._distribution_rule_id = None
        self._statement_no = None
        self._trade_id = None
        self._write_off_amount = None
        self._write_off_time = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def distribution_pro_no(self):
        return self._distribution_pro_no

    @distribution_pro_no.setter
    def distribution_pro_no(self, value):
        self._distribution_pro_no = value
    @property
    def distribution_rule_id(self):
        return self._distribution_rule_id

    @distribution_rule_id.setter
    def distribution_rule_id(self, value):
        self._distribution_rule_id = value
    @property
    def statement_no(self):
        return self._statement_no

    @statement_no.setter
    def statement_no(self, value):
        self._statement_no = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def write_off_amount(self):
        return self._write_off_amount

    @write_off_amount.setter
    def write_off_amount(self, value):
        self._write_off_amount = value
    @property
    def write_off_time(self):
        return self._write_off_time

    @write_off_time.setter
    def write_off_time(self, value):
        self._write_off_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.distribution_pro_no:
            if hasattr(self.distribution_pro_no, 'to_alipay_dict'):
                params['distribution_pro_no'] = self.distribution_pro_no.to_alipay_dict()
            else:
                params['distribution_pro_no'] = self.distribution_pro_no
        if self.distribution_rule_id:
            if hasattr(self.distribution_rule_id, 'to_alipay_dict'):
                params['distribution_rule_id'] = self.distribution_rule_id.to_alipay_dict()
            else:
                params['distribution_rule_id'] = self.distribution_rule_id
        if self.statement_no:
            if hasattr(self.statement_no, 'to_alipay_dict'):
                params['statement_no'] = self.statement_no.to_alipay_dict()
            else:
                params['statement_no'] = self.statement_no
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        if self.write_off_amount:
            if hasattr(self.write_off_amount, 'to_alipay_dict'):
                params['write_off_amount'] = self.write_off_amount.to_alipay_dict()
            else:
                params['write_off_amount'] = self.write_off_amount
        if self.write_off_time:
            if hasattr(self.write_off_time, 'to_alipay_dict'):
                params['write_off_time'] = self.write_off_time.to_alipay_dict()
            else:
                params['write_off_time'] = self.write_off_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceIncomeStatementVerifyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'distribution_pro_no' in d:
            o.distribution_pro_no = d['distribution_pro_no']
        if 'distribution_rule_id' in d:
            o.distribution_rule_id = d['distribution_rule_id']
        if 'statement_no' in d:
            o.statement_no = d['statement_no']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'write_off_amount' in d:
            o.write_off_amount = d['write_off_amount']
        if 'write_off_time' in d:
            o.write_off_time = d['write_off_time']
        return o


