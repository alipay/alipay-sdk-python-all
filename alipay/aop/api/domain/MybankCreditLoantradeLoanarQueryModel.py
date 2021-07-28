#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeLoanarQueryModel(object):

    def __init__(self):
        self._iproleid = None
        self._loanarno = None
        self._roletype = None

    @property
    def iproleid(self):
        return self._iproleid

    @iproleid.setter
    def iproleid(self, value):
        self._iproleid = value
    @property
    def loanarno(self):
        return self._loanarno

    @loanarno.setter
    def loanarno(self, value):
        self._loanarno = value
    @property
    def roletype(self):
        return self._roletype

    @roletype.setter
    def roletype(self, value):
        self._roletype = value


    def to_alipay_dict(self):
        params = dict()
        if self.iproleid:
            if hasattr(self.iproleid, 'to_alipay_dict'):
                params['iproleid'] = self.iproleid.to_alipay_dict()
            else:
                params['iproleid'] = self.iproleid
        if self.loanarno:
            if hasattr(self.loanarno, 'to_alipay_dict'):
                params['loanarno'] = self.loanarno.to_alipay_dict()
            else:
                params['loanarno'] = self.loanarno
        if self.roletype:
            if hasattr(self.roletype, 'to_alipay_dict'):
                params['roletype'] = self.roletype.to_alipay_dict()
            else:
                params['roletype'] = self.roletype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeLoanarQueryModel()
        if 'iproleid' in d:
            o.iproleid = d['iproleid']
        if 'loanarno' in d:
            o.loanarno = d['loanarno']
        if 'roletype' in d:
            o.roletype = d['roletype']
        return o


