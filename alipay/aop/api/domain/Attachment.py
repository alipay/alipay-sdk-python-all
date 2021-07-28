#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Attachment(object):

    def __init__(self):
        self._attachment_name = None
        self._file_id = None

    @property
    def attachment_name(self):
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self._attachment_name = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_name:
            if hasattr(self.attachment_name, 'to_alipay_dict'):
                params['attachment_name'] = self.attachment_name.to_alipay_dict()
            else:
                params['attachment_name'] = self.attachment_name
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Attachment()
        if 'attachment_name' in d:
            o.attachment_name = d['attachment_name']
        if 'file_id' in d:
            o.file_id = d['file_id']
        return o


