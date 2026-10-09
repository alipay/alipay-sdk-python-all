#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayPosterAppQueryModel(object):

    def __init__(self):
        self._biz_tid = None
        self._business_id = None
        self._interaction_type = None
        self._item_id = None
        self._item_type = None
        self._program_version = None
        self._schema_id = None
        self._use_cache = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def interaction_type(self):
        return self._interaction_type

    @interaction_type.setter
    def interaction_type(self, value):
        self._interaction_type = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def program_version(self):
        return self._program_version

    @program_version.setter
    def program_version(self, value):
        self._program_version = value
    @property
    def schema_id(self):
        return self._schema_id

    @schema_id.setter
    def schema_id(self, value):
        self._schema_id = value
    @property
    def use_cache(self):
        return self._use_cache

    @use_cache.setter
    def use_cache(self, value):
        self._use_cache = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.interaction_type:
            if hasattr(self.interaction_type, 'to_alipay_dict'):
                params['interaction_type'] = self.interaction_type.to_alipay_dict()
            else:
                params['interaction_type'] = self.interaction_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.program_version:
            if hasattr(self.program_version, 'to_alipay_dict'):
                params['program_version'] = self.program_version.to_alipay_dict()
            else:
                params['program_version'] = self.program_version
        if self.schema_id:
            if hasattr(self.schema_id, 'to_alipay_dict'):
                params['schema_id'] = self.schema_id.to_alipay_dict()
            else:
                params['schema_id'] = self.schema_id
        if self.use_cache:
            if hasattr(self.use_cache, 'to_alipay_dict'):
                params['use_cache'] = self.use_cache.to_alipay_dict()
            else:
                params['use_cache'] = self.use_cache
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayPosterAppQueryModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'interaction_type' in d:
            o.interaction_type = d['interaction_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'program_version' in d:
            o.program_version = d['program_version']
        if 'schema_id' in d:
            o.schema_id = d['schema_id']
        if 'use_cache' in d:
            o.use_cache = d['use_cache']
        return o


