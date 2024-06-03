#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenContentGoodsCheckResult import OpenContentGoodsCheckResult


class LiveStoreItemInfoDTO(object):

    def __init__(self):
        self._check_result = None
        self._in_store = None
        self._item_id = None

    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        if isinstance(value, OpenContentGoodsCheckResult):
            self._check_result = value
        else:
            self._check_result = OpenContentGoodsCheckResult.from_alipay_dict(value)
    @property
    def in_store(self):
        return self._in_store

    @in_store.setter
    def in_store(self, value):
        self._in_store = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_result:
            if hasattr(self.check_result, 'to_alipay_dict'):
                params['check_result'] = self.check_result.to_alipay_dict()
            else:
                params['check_result'] = self.check_result
        if self.in_store:
            if hasattr(self.in_store, 'to_alipay_dict'):
                params['in_store'] = self.in_store.to_alipay_dict()
            else:
                params['in_store'] = self.in_store
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LiveStoreItemInfoDTO()
        if 'check_result' in d:
            o.check_result = d['check_result']
        if 'in_store' in d:
            o.in_store = d['in_store']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


