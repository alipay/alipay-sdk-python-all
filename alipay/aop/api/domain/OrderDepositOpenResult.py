#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderDepositOpenResult(object):

    def __init__(self):
        self._deposit_amount = None
        self._deposit_direction = None
        self._deposit_id = None
        self._deposit_status = None
        self._gmt_modified = None

    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def deposit_direction(self):
        return self._deposit_direction

    @deposit_direction.setter
    def deposit_direction(self, value):
        self._deposit_direction = value
    @property
    def deposit_id(self):
        return self._deposit_id

    @deposit_id.setter
    def deposit_id(self, value):
        self._deposit_id = value
    @property
    def deposit_status(self):
        return self._deposit_status

    @deposit_status.setter
    def deposit_status(self, value):
        self._deposit_status = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value


    def to_alipay_dict(self):
        params = dict()
        if self.deposit_amount:
            if hasattr(self.deposit_amount, 'to_alipay_dict'):
                params['deposit_amount'] = self.deposit_amount.to_alipay_dict()
            else:
                params['deposit_amount'] = self.deposit_amount
        if self.deposit_direction:
            if hasattr(self.deposit_direction, 'to_alipay_dict'):
                params['deposit_direction'] = self.deposit_direction.to_alipay_dict()
            else:
                params['deposit_direction'] = self.deposit_direction
        if self.deposit_id:
            if hasattr(self.deposit_id, 'to_alipay_dict'):
                params['deposit_id'] = self.deposit_id.to_alipay_dict()
            else:
                params['deposit_id'] = self.deposit_id
        if self.deposit_status:
            if hasattr(self.deposit_status, 'to_alipay_dict'):
                params['deposit_status'] = self.deposit_status.to_alipay_dict()
            else:
                params['deposit_status'] = self.deposit_status
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderDepositOpenResult()
        if 'deposit_amount' in d:
            o.deposit_amount = d['deposit_amount']
        if 'deposit_direction' in d:
            o.deposit_direction = d['deposit_direction']
        if 'deposit_id' in d:
            o.deposit_id = d['deposit_id']
        if 'deposit_status' in d:
            o.deposit_status = d['deposit_status']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        return o


