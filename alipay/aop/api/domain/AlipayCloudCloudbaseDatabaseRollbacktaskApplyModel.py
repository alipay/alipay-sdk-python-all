#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MongoRollbackCollection import MongoRollbackCollection


class AlipayCloudCloudbaseDatabaseRollbacktaskApplyModel(object):

    def __init__(self):
        self._archive_time = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._rollback_collections = None

    @property
    def archive_time(self):
        return self._archive_time

    @archive_time.setter
    def archive_time(self, value):
        self._archive_time = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def rollback_collections(self):
        return self._rollback_collections

    @rollback_collections.setter
    def rollback_collections(self, value):
        if isinstance(value, list):
            self._rollback_collections = list()
            for i in value:
                if isinstance(i, MongoRollbackCollection):
                    self._rollback_collections.append(i)
                else:
                    self._rollback_collections.append(MongoRollbackCollection.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.archive_time:
            if hasattr(self.archive_time, 'to_alipay_dict'):
                params['archive_time'] = self.archive_time.to_alipay_dict()
            else:
                params['archive_time'] = self.archive_time
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
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
        o = AlipayCloudCloudbaseDatabaseRollbacktaskApplyModel()
        if 'archive_time' in d:
            o.archive_time = d['archive_time']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'rollback_collections' in d:
            o.rollback_collections = d['rollback_collections']
        return o


