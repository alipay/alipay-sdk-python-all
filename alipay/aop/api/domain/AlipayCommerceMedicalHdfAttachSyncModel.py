#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfAttachSyncModel(object):

    def __init__(self):
        self._action = None
        self._attachment_id = None
        self._file_name = None
        self._file_path = None
        self._is_format = None
        self._mime = None
        self._owner_id = None
        self._owner_type = None
        self._related_id = None
        self._related_type = None
        self._size = None
        self._type = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, value):
        self._attachment_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def is_format(self):
        return self._is_format

    @is_format.setter
    def is_format(self, value):
        self._is_format = value
    @property
    def mime(self):
        return self._mime

    @mime.setter
    def mime(self, value):
        self._mime = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def related_id(self):
        return self._related_id

    @related_id.setter
    def related_id(self, value):
        self._related_id = value
    @property
    def related_type(self):
        return self._related_type

    @related_type.setter
    def related_type(self, value):
        self._related_type = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.attachment_id:
            if hasattr(self.attachment_id, 'to_alipay_dict'):
                params['attachment_id'] = self.attachment_id.to_alipay_dict()
            else:
                params['attachment_id'] = self.attachment_id
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.is_format:
            if hasattr(self.is_format, 'to_alipay_dict'):
                params['is_format'] = self.is_format.to_alipay_dict()
            else:
                params['is_format'] = self.is_format
        if self.mime:
            if hasattr(self.mime, 'to_alipay_dict'):
                params['mime'] = self.mime.to_alipay_dict()
            else:
                params['mime'] = self.mime
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.related_id:
            if hasattr(self.related_id, 'to_alipay_dict'):
                params['related_id'] = self.related_id.to_alipay_dict()
            else:
                params['related_id'] = self.related_id
        if self.related_type:
            if hasattr(self.related_type, 'to_alipay_dict'):
                params['related_type'] = self.related_type.to_alipay_dict()
            else:
                params['related_type'] = self.related_type
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfAttachSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'attachment_id' in d:
            o.attachment_id = d['attachment_id']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'is_format' in d:
            o.is_format = d['is_format']
        if 'mime' in d:
            o.mime = d['mime']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'related_id' in d:
            o.related_id = d['related_id']
        if 'related_type' in d:
            o.related_type = d['related_type']
        if 'size' in d:
            o.size = d['size']
        if 'type' in d:
            o.type = d['type']
        return o


