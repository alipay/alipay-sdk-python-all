#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundTransferLogResult(object):

    def __init__(self):
        self._amount = None
        self._fail_reason = None
        self._remark = None
        self._source_account = None
        self._status = None
        self._target_account = None
        self._trans_create_time = None
        self._trans_date = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def source_account(self):
        return self._source_account

    @source_account.setter
    def source_account(self, value):
        self._source_account = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_account(self):
        return self._target_account

    @target_account.setter
    def target_account(self, value):
        self._target_account = value
    @property
    def trans_create_time(self):
        return self._trans_create_time

    @trans_create_time.setter
    def trans_create_time(self, value):
        self._trans_create_time = value
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.source_account:
            if hasattr(self.source_account, 'to_alipay_dict'):
                params['source_account'] = self.source_account.to_alipay_dict()
            else:
                params['source_account'] = self.source_account
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_account:
            if hasattr(self.target_account, 'to_alipay_dict'):
                params['target_account'] = self.target_account.to_alipay_dict()
            else:
                params['target_account'] = self.target_account
        if self.trans_create_time:
            if hasattr(self.trans_create_time, 'to_alipay_dict'):
                params['trans_create_time'] = self.trans_create_time.to_alipay_dict()
            else:
                params['trans_create_time'] = self.trans_create_time
        if self.trans_date:
            if hasattr(self.trans_date, 'to_alipay_dict'):
                params['trans_date'] = self.trans_date.to_alipay_dict()
            else:
                params['trans_date'] = self.trans_date
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundTransferLogResult()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'remark' in d:
            o.remark = d['remark']
        if 'source_account' in d:
            o.source_account = d['source_account']
        if 'status' in d:
            o.status = d['status']
        if 'target_account' in d:
            o.target_account = d['target_account']
        if 'trans_create_time' in d:
            o.trans_create_time = d['trans_create_time']
        if 'trans_date' in d:
            o.trans_date = d['trans_date']
        if 'type' in d:
            o.type = d['type']
        return o


