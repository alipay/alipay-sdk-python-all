#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationTagClaimModifyModel(object):

    def __init__(self):
        self._new_alipay_account = None
        self._old_alipay_account = None
        self._store_id = None
        self._store_id_type = None

    @property
    def new_alipay_account(self):
        return self._new_alipay_account

    @new_alipay_account.setter
    def new_alipay_account(self, value):
        self._new_alipay_account = value
    @property
    def old_alipay_account(self):
        return self._old_alipay_account

    @old_alipay_account.setter
    def old_alipay_account(self, value):
        self._old_alipay_account = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_id_type(self):
        return self._store_id_type

    @store_id_type.setter
    def store_id_type(self, value):
        self._store_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_alipay_account:
            if hasattr(self.new_alipay_account, 'to_alipay_dict'):
                params['new_alipay_account'] = self.new_alipay_account.to_alipay_dict()
            else:
                params['new_alipay_account'] = self.new_alipay_account
        if self.old_alipay_account:
            if hasattr(self.old_alipay_account, 'to_alipay_dict'):
                params['old_alipay_account'] = self.old_alipay_account.to_alipay_dict()
            else:
                params['old_alipay_account'] = self.old_alipay_account
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_id_type:
            if hasattr(self.store_id_type, 'to_alipay_dict'):
                params['store_id_type'] = self.store_id_type.to_alipay_dict()
            else:
                params['store_id_type'] = self.store_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationTagClaimModifyModel()
        if 'new_alipay_account' in d:
            o.new_alipay_account = d['new_alipay_account']
        if 'old_alipay_account' in d:
            o.old_alipay_account = d['old_alipay_account']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_id_type' in d:
            o.store_id_type = d['store_id_type']
        return o


