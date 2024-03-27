#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MongoRollbackCollection(object):

    def __init__(self):
        self._rollback_collection_name = None
        self._source_collection_name = None

    @property
    def rollback_collection_name(self):
        return self._rollback_collection_name

    @rollback_collection_name.setter
    def rollback_collection_name(self, value):
        self._rollback_collection_name = value
    @property
    def source_collection_name(self):
        return self._source_collection_name

    @source_collection_name.setter
    def source_collection_name(self, value):
        self._source_collection_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.rollback_collection_name:
            if hasattr(self.rollback_collection_name, 'to_alipay_dict'):
                params['rollback_collection_name'] = self.rollback_collection_name.to_alipay_dict()
            else:
                params['rollback_collection_name'] = self.rollback_collection_name
        if self.source_collection_name:
            if hasattr(self.source_collection_name, 'to_alipay_dict'):
                params['source_collection_name'] = self.source_collection_name.to_alipay_dict()
            else:
                params['source_collection_name'] = self.source_collection_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MongoRollbackCollection()
        if 'rollback_collection_name' in d:
            o.rollback_collection_name = d['rollback_collection_name']
        if 'source_collection_name' in d:
            o.source_collection_name = d['source_collection_name']
        return o


