#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCplifeBillSyncModel(object):

    def __init__(self):
        self._bill_entry_id = None
        self._community_id = None
        self._new_deadline = None
        self._new_entry_amount = None
        self._operate_type = None

    @property
    def bill_entry_id(self):
        return self._bill_entry_id

    @bill_entry_id.setter
    def bill_entry_id(self, value):
        self._bill_entry_id = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def new_deadline(self):
        return self._new_deadline

    @new_deadline.setter
    def new_deadline(self, value):
        self._new_deadline = value
    @property
    def new_entry_amount(self):
        return self._new_entry_amount

    @new_entry_amount.setter
    def new_entry_amount(self, value):
        self._new_entry_amount = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_entry_id:
            if hasattr(self.bill_entry_id, 'to_alipay_dict'):
                params['bill_entry_id'] = self.bill_entry_id.to_alipay_dict()
            else:
                params['bill_entry_id'] = self.bill_entry_id
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.new_deadline:
            if hasattr(self.new_deadline, 'to_alipay_dict'):
                params['new_deadline'] = self.new_deadline.to_alipay_dict()
            else:
                params['new_deadline'] = self.new_deadline
        if self.new_entry_amount:
            if hasattr(self.new_entry_amount, 'to_alipay_dict'):
                params['new_entry_amount'] = self.new_entry_amount.to_alipay_dict()
            else:
                params['new_entry_amount'] = self.new_entry_amount
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeBillSyncModel()
        if 'bill_entry_id' in d:
            o.bill_entry_id = d['bill_entry_id']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'new_deadline' in d:
            o.new_deadline = d['new_deadline']
        if 'new_entry_amount' in d:
            o.new_entry_amount = d['new_entry_amount']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


