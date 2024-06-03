#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalAuthorizeQueryModel(object):

    def __init__(self):
        self._ftoken = None
        self._open_id = None
        self._org_no = None
        self._user_id = None

    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_no:
            if hasattr(self.org_no, 'to_alipay_dict'):
                params['org_no'] = self.org_no.to_alipay_dict()
            else:
                params['org_no'] = self.org_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAuthorizeQueryModel()
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_no' in d:
            o.org_no = d['org_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


