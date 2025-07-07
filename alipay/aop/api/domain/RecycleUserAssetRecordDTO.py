#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleUserAssetRecordDTO(object):

    def __init__(self):
        self._amount = None
        self._asset_type = None
        self._gmt_create = None
        self._gmt_modified = None
        self._order_id = None
        self._record_id = None
        self._record_status = None
        self._record_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def record_status(self):
        return self._record_status

    @record_status.setter
    def record_status(self, value):
        self._record_status = value
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.record_status:
            if hasattr(self.record_status, 'to_alipay_dict'):
                params['record_status'] = self.record_status.to_alipay_dict()
            else:
                params['record_status'] = self.record_status
        if self.record_type:
            if hasattr(self.record_type, 'to_alipay_dict'):
                params['record_type'] = self.record_type.to_alipay_dict()
            else:
                params['record_type'] = self.record_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleUserAssetRecordDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'record_status' in d:
            o.record_status = d['record_status']
        if 'record_type' in d:
            o.record_type = d['record_type']
        return o


