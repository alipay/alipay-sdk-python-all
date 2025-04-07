#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantRelationEntity(object):

    def __init__(self):
        self._memo = None
        self._seller_id = None
        self._seller_open_id = None
        self._sub_seller_id = None
        self._sub_seller_open_id = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_open_id(self):
        return self._seller_open_id

    @seller_open_id.setter
    def seller_open_id(self, value):
        self._seller_open_id = value
    @property
    def sub_seller_id(self):
        return self._sub_seller_id

    @sub_seller_id.setter
    def sub_seller_id(self, value):
        self._sub_seller_id = value
    @property
    def sub_seller_open_id(self):
        return self._sub_seller_open_id

    @sub_seller_open_id.setter
    def sub_seller_open_id(self, value):
        self._sub_seller_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_open_id:
            if hasattr(self.seller_open_id, 'to_alipay_dict'):
                params['seller_open_id'] = self.seller_open_id.to_alipay_dict()
            else:
                params['seller_open_id'] = self.seller_open_id
        if self.sub_seller_id:
            if hasattr(self.sub_seller_id, 'to_alipay_dict'):
                params['sub_seller_id'] = self.sub_seller_id.to_alipay_dict()
            else:
                params['sub_seller_id'] = self.sub_seller_id
        if self.sub_seller_open_id:
            if hasattr(self.sub_seller_open_id, 'to_alipay_dict'):
                params['sub_seller_open_id'] = self.sub_seller_open_id.to_alipay_dict()
            else:
                params['sub_seller_open_id'] = self.sub_seller_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantRelationEntity()
        if 'memo' in d:
            o.memo = d['memo']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_open_id' in d:
            o.seller_open_id = d['seller_open_id']
        if 'sub_seller_id' in d:
            o.sub_seller_id = d['sub_seller_id']
        if 'sub_seller_open_id' in d:
            o.sub_seller_open_id = d['sub_seller_open_id']
        return o


