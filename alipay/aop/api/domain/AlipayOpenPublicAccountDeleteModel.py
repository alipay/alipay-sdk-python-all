#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicAccountDeleteModel(object):

    def __init__(self):
        self._agreement_id = None
        self._bind_account_no = None

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
        return o


