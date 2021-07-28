#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainTwcUserinfoMatchModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._call_no_hash = None
        self._unify_no = None
        self._unify_no_hash = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def call_no_hash(self):
        return self._call_no_hash

    @call_no_hash.setter
    def call_no_hash(self, value):
        self._call_no_hash = value
    @property
    def unify_no(self):
        return self._unify_no

    @unify_no.setter
    def unify_no(self, value):
        self._unify_no = value
    @property
    def unify_no_hash(self):
        return self._unify_no_hash

    @unify_no_hash.setter
    def unify_no_hash(self, value):
        self._unify_no_hash = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.call_no_hash:
            if hasattr(self.call_no_hash, 'to_alipay_dict'):
                params['call_no_hash'] = self.call_no_hash.to_alipay_dict()
            else:
                params['call_no_hash'] = self.call_no_hash
        if self.unify_no:
            if hasattr(self.unify_no, 'to_alipay_dict'):
                params['unify_no'] = self.unify_no.to_alipay_dict()
            else:
                params['unify_no'] = self.unify_no
        if self.unify_no_hash:
            if hasattr(self.unify_no_hash, 'to_alipay_dict'):
                params['unify_no_hash'] = self.unify_no_hash.to_alipay_dict()
            else:
                params['unify_no_hash'] = self.unify_no_hash
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainTwcUserinfoMatchModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'call_no_hash' in d:
            o.call_no_hash = d['call_no_hash']
        if 'unify_no' in d:
            o.unify_no = d['unify_no']
        if 'unify_no_hash' in d:
            o.unify_no_hash = d['unify_no_hash']
        return o


