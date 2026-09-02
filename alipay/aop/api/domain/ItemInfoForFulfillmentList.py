#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemInfoForFulfillmentList(object):

    def __init__(self):
        self._is_deleted = None
        self._relation_spu_id = None
        self._sku_code = None
        self._sku_id = None
        self._spu_id = None

    @property
    def is_deleted(self):
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, value):
        self._is_deleted = value
    @property
    def relation_spu_id(self):
        return self._relation_spu_id

    @relation_spu_id.setter
    def relation_spu_id(self, value):
        self._relation_spu_id = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_deleted:
            if hasattr(self.is_deleted, 'to_alipay_dict'):
                params['is_deleted'] = self.is_deleted.to_alipay_dict()
            else:
                params['is_deleted'] = self.is_deleted
        if self.relation_spu_id:
            if hasattr(self.relation_spu_id, 'to_alipay_dict'):
                params['relation_spu_id'] = self.relation_spu_id.to_alipay_dict()
            else:
                params['relation_spu_id'] = self.relation_spu_id
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemInfoForFulfillmentList()
        if 'is_deleted' in d:
            o.is_deleted = d['is_deleted']
        if 'relation_spu_id' in d:
            o.relation_spu_id = d['relation_spu_id']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        return o


