#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetReverseDetail(object):

    def __init__(self):
        self._amount = None
        self._assign_item_id = None
        self._batch_no = None
        self._goods_status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def goods_status(self):
        return self._goods_status

    @goods_status.setter
    def goods_status(self, value):
        self._goods_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.goods_status:
            if hasattr(self.goods_status, 'to_alipay_dict'):
                params['goods_status'] = self.goods_status.to_alipay_dict()
            else:
                params['goods_status'] = self.goods_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetReverseDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'goods_status' in d:
            o.goods_status = d['goods_status']
        return o


