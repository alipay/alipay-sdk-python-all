#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSettleEfundUnfreezeModel(object):

    def __init__(self):
        self._amount = None
        self._extend_params = None
        self._memo = None
        self._out_request_no = None
        self._seller_open_id = None
        self._seller_user_id = None
        self._settle_biz_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def seller_open_id(self):
        return self._seller_open_id

    @seller_open_id.setter
    def seller_open_id(self, value):
        self._seller_open_id = value
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value
    @property
    def settle_biz_type(self):
        return self._settle_biz_type

    @settle_biz_type.setter
    def settle_biz_type(self, value):
        self._settle_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.seller_open_id:
            if hasattr(self.seller_open_id, 'to_alipay_dict'):
                params['seller_open_id'] = self.seller_open_id.to_alipay_dict()
            else:
                params['seller_open_id'] = self.seller_open_id
        if self.seller_user_id:
            if hasattr(self.seller_user_id, 'to_alipay_dict'):
                params['seller_user_id'] = self.seller_user_id.to_alipay_dict()
            else:
                params['seller_user_id'] = self.seller_user_id
        if self.settle_biz_type:
            if hasattr(self.settle_biz_type, 'to_alipay_dict'):
                params['settle_biz_type'] = self.settle_biz_type.to_alipay_dict()
            else:
                params['settle_biz_type'] = self.settle_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSettleEfundUnfreezeModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'seller_open_id' in d:
            o.seller_open_id = d['seller_open_id']
        if 'seller_user_id' in d:
            o.seller_user_id = d['seller_user_id']
        if 'settle_biz_type' in d:
            o.settle_biz_type = d['settle_biz_type']
        return o


