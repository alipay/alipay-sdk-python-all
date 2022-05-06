#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTuitioncodeMonitorCreateModel(object):

    def __init__(self):
        self._bank_type = None
        self._login_account = None
        self._out_apply_id = None
        self._parent_no = None

    @property
    def bank_type(self):
        return self._bank_type

    @bank_type.setter
    def bank_type(self, value):
        self._bank_type = value
    @property
    def login_account(self):
        return self._login_account

    @login_account.setter
    def login_account(self, value):
        self._login_account = value
    @property
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value
    @property
    def parent_no(self):
        return self._parent_no

    @parent_no.setter
    def parent_no(self, value):
        self._parent_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_type:
            if hasattr(self.bank_type, 'to_alipay_dict'):
                params['bank_type'] = self.bank_type.to_alipay_dict()
            else:
                params['bank_type'] = self.bank_type
        if self.login_account:
            if hasattr(self.login_account, 'to_alipay_dict'):
                params['login_account'] = self.login_account.to_alipay_dict()
            else:
                params['login_account'] = self.login_account
        if self.out_apply_id:
            if hasattr(self.out_apply_id, 'to_alipay_dict'):
                params['out_apply_id'] = self.out_apply_id.to_alipay_dict()
            else:
                params['out_apply_id'] = self.out_apply_id
        if self.parent_no:
            if hasattr(self.parent_no, 'to_alipay_dict'):
                params['parent_no'] = self.parent_no.to_alipay_dict()
            else:
                params['parent_no'] = self.parent_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTuitioncodeMonitorCreateModel()
        if 'bank_type' in d:
            o.bank_type = d['bank_type']
        if 'login_account' in d:
            o.login_account = d['login_account']
        if 'out_apply_id' in d:
            o.out_apply_id = d['out_apply_id']
        if 'parent_no' in d:
            o.parent_no = d['parent_no']
        return o


