#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentData import ContentData


class AlipayCommerceMedicalHealthArchiveSyncModel(object):

    def __init__(self):
        self._content_data = None
        self._data_source = None
        self._data_type = None
        self._open_id = None
        self._sync_status = None
        self._sync_type = None
        self._task_id = None
        self._user_id = None

    @property
    def content_data(self):
        return self._content_data

    @content_data.setter
    def content_data(self, value):
        if isinstance(value, ContentData):
            self._content_data = value
        else:
            self._content_data = ContentData.from_alipay_dict(value)
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def sync_status(self):
        return self._sync_status

    @sync_status.setter
    def sync_status(self, value):
        self._sync_status = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_data:
            if hasattr(self.content_data, 'to_alipay_dict'):
                params['content_data'] = self.content_data.to_alipay_dict()
            else:
                params['content_data'] = self.content_data
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.sync_status:
            if hasattr(self.sync_status, 'to_alipay_dict'):
                params['sync_status'] = self.sync_status.to_alipay_dict()
            else:
                params['sync_status'] = self.sync_status
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthArchiveSyncModel()
        if 'content_data' in d:
            o.content_data = d['content_data']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'sync_status' in d:
            o.sync_status = d['sync_status']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


