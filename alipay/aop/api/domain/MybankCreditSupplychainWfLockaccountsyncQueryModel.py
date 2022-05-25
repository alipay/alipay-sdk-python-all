#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Lockaccountsync import Lockaccountsync


class MybankCreditSupplychainWfLockaccountsyncQueryModel(object):

    def __init__(self):
        self._lockaccountsyncs = None
        self._requestid = None

    @property
    def lockaccountsyncs(self):
        return self._lockaccountsyncs

    @lockaccountsyncs.setter
    def lockaccountsyncs(self, value):
        if isinstance(value, list):
            self._lockaccountsyncs = list()
            for i in value:
                if isinstance(i, Lockaccountsync):
                    self._lockaccountsyncs.append(i)
                else:
                    self._lockaccountsyncs.append(Lockaccountsync.from_alipay_dict(i))
    @property
    def requestid(self):
        return self._requestid

    @requestid.setter
    def requestid(self, value):
        self._requestid = value


    def to_alipay_dict(self):
        params = dict()
        if self.lockaccountsyncs:
            if isinstance(self.lockaccountsyncs, list):
                for i in range(0, len(self.lockaccountsyncs)):
                    element = self.lockaccountsyncs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.lockaccountsyncs[i] = element.to_alipay_dict()
            if hasattr(self.lockaccountsyncs, 'to_alipay_dict'):
                params['lockaccountsyncs'] = self.lockaccountsyncs.to_alipay_dict()
            else:
                params['lockaccountsyncs'] = self.lockaccountsyncs
        if self.requestid:
            if hasattr(self.requestid, 'to_alipay_dict'):
                params['requestid'] = self.requestid.to_alipay_dict()
            else:
                params['requestid'] = self.requestid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainWfLockaccountsyncQueryModel()
        if 'lockaccountsyncs' in d:
            o.lockaccountsyncs = d['lockaccountsyncs']
        if 'requestid' in d:
            o.requestid = d['requestid']
        return o


