#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleRoyaltyInfo(object):

    def __init__(self):
        self._amount = None
        self._desc = None
        self._role_type = None
        self._trans_in = None
        self._trans_in_login_id = None
        self._trans_in_open_id = None
        self._trans_in_type = None
        self._trans_stage = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def trans_in_login_id(self):
        return self._trans_in_login_id

    @trans_in_login_id.setter
    def trans_in_login_id(self, value):
        self._trans_in_login_id = value
    @property
    def trans_in_open_id(self):
        return self._trans_in_open_id

    @trans_in_open_id.setter
    def trans_in_open_id(self, value):
        self._trans_in_open_id = value
    @property
    def trans_in_type(self):
        return self._trans_in_type

    @trans_in_type.setter
    def trans_in_type(self, value):
        self._trans_in_type = value
    @property
    def trans_stage(self):
        return self._trans_stage

    @trans_stage.setter
    def trans_stage(self, value):
        self._trans_stage = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.trans_in_login_id:
            if hasattr(self.trans_in_login_id, 'to_alipay_dict'):
                params['trans_in_login_id'] = self.trans_in_login_id.to_alipay_dict()
            else:
                params['trans_in_login_id'] = self.trans_in_login_id
        if self.trans_in_open_id:
            if hasattr(self.trans_in_open_id, 'to_alipay_dict'):
                params['trans_in_open_id'] = self.trans_in_open_id.to_alipay_dict()
            else:
                params['trans_in_open_id'] = self.trans_in_open_id
        if self.trans_in_type:
            if hasattr(self.trans_in_type, 'to_alipay_dict'):
                params['trans_in_type'] = self.trans_in_type.to_alipay_dict()
            else:
                params['trans_in_type'] = self.trans_in_type
        if self.trans_stage:
            if hasattr(self.trans_stage, 'to_alipay_dict'):
                params['trans_stage'] = self.trans_stage.to_alipay_dict()
            else:
                params['trans_stage'] = self.trans_stage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleRoyaltyInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'desc' in d:
            o.desc = d['desc']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_login_id' in d:
            o.trans_in_login_id = d['trans_in_login_id']
        if 'trans_in_open_id' in d:
            o.trans_in_open_id = d['trans_in_open_id']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        if 'trans_stage' in d:
            o.trans_stage = d['trans_stage']
        return o


