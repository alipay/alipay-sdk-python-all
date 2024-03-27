#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MongoRollbackTaskDetail(object):

    def __init__(self):
        self._detail_id = None
        self._process = None
        self._rollback_collection_name = None
        self._source_collection_name = None
        self._status = None

    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def process(self):
        return self._process

    @process.setter
    def process(self, value):
        self._process = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.process:
            if hasattr(self.process, 'to_alipay_dict'):
                params['process'] = self.process.to_alipay_dict()
            else:
                params['process'] = self.process
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MongoRollbackTaskDetail()
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'process' in d:
            o.process = d['process']
        if 'rollback_collection_name' in d:
            o.rollback_collection_name = d['rollback_collection_name']
        if 'source_collection_name' in d:
            o.source_collection_name = d['source_collection_name']
        if 'status' in d:
            o.status = d['status']
        return o


