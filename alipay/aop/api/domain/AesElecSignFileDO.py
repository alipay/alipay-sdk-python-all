#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AesElecSignFileDO(object):

    def __init__(self):
        self._file_id = None
        self._file_key = None
        self._file_name = None
        self._file_type = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._related_process_id = None
        self._sign_task_id = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def related_process_id(self):
        return self._related_process_id

    @related_process_id.setter
    def related_process_id(self, value):
        self._related_process_id = value
    @property
    def sign_task_id(self):
        return self._sign_task_id

    @sign_task_id.setter
    def sign_task_id(self, value):
        self._sign_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.related_process_id:
            if hasattr(self.related_process_id, 'to_alipay_dict'):
                params['related_process_id'] = self.related_process_id.to_alipay_dict()
            else:
                params['related_process_id'] = self.related_process_id
        if self.sign_task_id:
            if hasattr(self.sign_task_id, 'to_alipay_dict'):
                params['sign_task_id'] = self.sign_task_id.to_alipay_dict()
            else:
                params['sign_task_id'] = self.sign_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AesElecSignFileDO()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'related_process_id' in d:
            o.related_process_id = d['related_process_id']
        if 'sign_task_id' in d:
            o.sign_task_id = d['sign_task_id']
        return o


