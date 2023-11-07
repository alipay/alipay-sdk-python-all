#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiMatterAttachmentDTO(object):

    def __init__(self):
        self._attachment_code = None
        self._attachment_name = None
        self._attachment_path = None
        self._attachment_url = None
        self._gmt_create = None
        self._gmt_modified = None
        self._matter_code = None

    @property
    def attachment_code(self):
        return self._attachment_code

    @attachment_code.setter
    def attachment_code(self, value):
        self._attachment_code = value
    @property
    def attachment_name(self):
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self._attachment_name = value
    @property
    def attachment_path(self):
        return self._attachment_path

    @attachment_path.setter
    def attachment_path(self, value):
        self._attachment_path = value
    @property
    def attachment_url(self):
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, value):
        self._attachment_url = value
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
    def matter_code(self):
        return self._matter_code

    @matter_code.setter
    def matter_code(self, value):
        self._matter_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_code:
            if hasattr(self.attachment_code, 'to_alipay_dict'):
                params['attachment_code'] = self.attachment_code.to_alipay_dict()
            else:
                params['attachment_code'] = self.attachment_code
        if self.attachment_name:
            if hasattr(self.attachment_name, 'to_alipay_dict'):
                params['attachment_name'] = self.attachment_name.to_alipay_dict()
            else:
                params['attachment_name'] = self.attachment_name
        if self.attachment_path:
            if hasattr(self.attachment_path, 'to_alipay_dict'):
                params['attachment_path'] = self.attachment_path.to_alipay_dict()
            else:
                params['attachment_path'] = self.attachment_path
        if self.attachment_url:
            if hasattr(self.attachment_url, 'to_alipay_dict'):
                params['attachment_url'] = self.attachment_url.to_alipay_dict()
            else:
                params['attachment_url'] = self.attachment_url
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
        if self.matter_code:
            if hasattr(self.matter_code, 'to_alipay_dict'):
                params['matter_code'] = self.matter_code.to_alipay_dict()
            else:
                params['matter_code'] = self.matter_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiMatterAttachmentDTO()
        if 'attachment_code' in d:
            o.attachment_code = d['attachment_code']
        if 'attachment_name' in d:
            o.attachment_name = d['attachment_name']
        if 'attachment_path' in d:
            o.attachment_path = d['attachment_path']
        if 'attachment_url' in d:
            o.attachment_url = d['attachment_url']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'matter_code' in d:
            o.matter_code = d['matter_code']
        return o


