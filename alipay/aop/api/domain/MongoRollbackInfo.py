#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MongoCollectionInfo import MongoCollectionInfo


class MongoRollbackInfo(object):

    def __init__(self):
        self._archive_time = None
        self._rollback_collections = None

    @property
    def archive_time(self):
        return self._archive_time

    @archive_time.setter
    def archive_time(self, value):
        self._archive_time = value
    @property
    def rollback_collections(self):
        return self._rollback_collections

    @rollback_collections.setter
    def rollback_collections(self, value):
        if isinstance(value, list):
            self._rollback_collections = list()
            for i in value:
                if isinstance(i, MongoCollectionInfo):
                    self._rollback_collections.append(i)
                else:
                    self._rollback_collections.append(MongoCollectionInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.archive_time:
            if hasattr(self.archive_time, 'to_alipay_dict'):
                params['archive_time'] = self.archive_time.to_alipay_dict()
            else:
                params['archive_time'] = self.archive_time
        if self.rollback_collections:
            if isinstance(self.rollback_collections, list):
                for i in range(0, len(self.rollback_collections)):
                    element = self.rollback_collections[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rollback_collections[i] = element.to_alipay_dict()
            if hasattr(self.rollback_collections, 'to_alipay_dict'):
                params['rollback_collections'] = self.rollback_collections.to_alipay_dict()
            else:
                params['rollback_collections'] = self.rollback_collections
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MongoRollbackInfo()
        if 'archive_time' in d:
            o.archive_time = d['archive_time']
        if 'rollback_collections' in d:
            o.rollback_collections = d['rollback_collections']
        return o


