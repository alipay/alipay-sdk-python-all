#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateDTO(object):

    def __init__(self):
        self._description = None
        self._file_name = None
        self._file_url = None
        self._gmt_create = None
        self._gmt_modified = None
        self._html_file_url = None
        self._id = None
        self._status = None
        self._template_code = None
        self._template_name = None
        self._version_no = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
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
    def html_file_url(self):
        return self._html_file_url

    @html_file_url.setter
    def html_file_url(self, value):
        self._html_file_url = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
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
        if self.html_file_url:
            if hasattr(self.html_file_url, 'to_alipay_dict'):
                params['html_file_url'] = self.html_file_url.to_alipay_dict()
            else:
                params['html_file_url'] = self.html_file_url
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateDTO()
        if 'description' in d:
            o.description = d['description']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'html_file_url' in d:
            o.html_file_url = d['html_file_url']
        if 'id' in d:
            o.id = d['id']
        if 'status' in d:
            o.status = d['status']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


