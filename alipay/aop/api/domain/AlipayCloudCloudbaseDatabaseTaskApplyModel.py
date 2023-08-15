#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseDatabaseTaskApplyModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._collection_name = None
        self._command = None
        self._conflict_mode = None
        self._fields = None
        self._file_type = None
        self._task_id = None
        self._upload_id = None

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
    def collection_name(self):
        return self._collection_name

    @collection_name.setter
    def collection_name(self, value):
        self._collection_name = value
    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value
    @property
    def conflict_mode(self):
        return self._conflict_mode

    @conflict_mode.setter
    def conflict_mode(self, value):
        self._conflict_mode = value
    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, list):
            self._fields = list()
            for i in value:
                self._fields.append(i)
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def upload_id(self):
        return self._upload_id

    @upload_id.setter
    def upload_id(self, value):
        self._upload_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.collection_name:
            if hasattr(self.collection_name, 'to_alipay_dict'):
                params['collection_name'] = self.collection_name.to_alipay_dict()
            else:
                params['collection_name'] = self.collection_name
        if self.command:
            if hasattr(self.command, 'to_alipay_dict'):
                params['command'] = self.command.to_alipay_dict()
            else:
                params['command'] = self.command
        if self.conflict_mode:
            if hasattr(self.conflict_mode, 'to_alipay_dict'):
                params['conflict_mode'] = self.conflict_mode.to_alipay_dict()
            else:
                params['conflict_mode'] = self.conflict_mode
        if self.fields:
            if isinstance(self.fields, list):
                for i in range(0, len(self.fields)):
                    element = self.fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fields[i] = element.to_alipay_dict()
            if hasattr(self.fields, 'to_alipay_dict'):
                params['fields'] = self.fields.to_alipay_dict()
            else:
                params['fields'] = self.fields
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.upload_id:
            if hasattr(self.upload_id, 'to_alipay_dict'):
                params['upload_id'] = self.upload_id.to_alipay_dict()
            else:
                params['upload_id'] = self.upload_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseDatabaseTaskApplyModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'collection_name' in d:
            o.collection_name = d['collection_name']
        if 'command' in d:
            o.command = d['command']
        if 'conflict_mode' in d:
            o.conflict_mode = d['conflict_mode']
        if 'fields' in d:
            o.fields = d['fields']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'upload_id' in d:
            o.upload_id = d['upload_id']
        return o


