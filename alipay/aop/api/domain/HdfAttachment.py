#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HdfAttachment(object):

    def __init__(self):
        self._attachment_id = None
        self._file_path = None
        self._owner_id = None

    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, value):
        self._attachment_id = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_id:
            if hasattr(self.attachment_id, 'to_alipay_dict'):
                params['attachment_id'] = self.attachment_id.to_alipay_dict()
            else:
                params['attachment_id'] = self.attachment_id
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HdfAttachment()
        if 'attachment_id' in d:
            o.attachment_id = d['attachment_id']
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        return o


