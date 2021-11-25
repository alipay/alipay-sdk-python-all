#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FtokenInfoQuery(object):

    def __init__(self):
        self._account = None
        self._bizid = None
        self._ftoken = None
        self._uid = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def bizid(self):
        return self._bizid

    @bizid.setter
    def bizid(self, value):
        self._bizid = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.bizid:
            if hasattr(self.bizid, 'to_alipay_dict'):
                params['bizid'] = self.bizid.to_alipay_dict()
            else:
                params['bizid'] = self.bizid
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FtokenInfoQuery()
        if 'account' in d:
            o.account = d['account']
        if 'bizid' in d:
            o.bizid = d['bizid']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'uid' in d:
            o.uid = d['uid']
        return o


