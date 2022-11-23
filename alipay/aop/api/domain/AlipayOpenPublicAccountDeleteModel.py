#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicAccountDeleteModel(object):

    def __init__(self):
        self._agreement_id = None
        self._bind_account_no = None
        self._from_user_id = None
        self._open_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def bind_account_no(self):
        return self._bind_account_no

    @bind_account_no.setter
    def bind_account_no(self, value):
        self._bind_account_no = value
    @property
    def from_user_id(self):
        return self._from_user_id

    @from_user_id.setter
    def from_user_id(self, value):
        self._from_user_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.bind_account_no:
            if hasattr(self.bind_account_no, 'to_alipay_dict'):
                params['bind_account_no'] = self.bind_account_no.to_alipay_dict()
            else:
                params['bind_account_no'] = self.bind_account_no
        if self.from_user_id:
            if hasattr(self.from_user_id, 'to_alipay_dict'):
                params['from_user_id'] = self.from_user_id.to_alipay_dict()
            else:
                params['from_user_id'] = self.from_user_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicAccountDeleteModel()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'bind_account_no' in d:
            o.bind_account_no = d['bind_account_no']
        if 'from_user_id' in d:
            o.from_user_id = d['from_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        return o


