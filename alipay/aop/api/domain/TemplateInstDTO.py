#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateInstDTO(object):

    def __init__(self):
        self._file_name = None
        self._html_oss_url = None
        self._html_preview_url = None
        self._inst_id = None
        self._oss_url = None
        self._preview_url = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def html_oss_url(self):
        return self._html_oss_url

    @html_oss_url.setter
    def html_oss_url(self, value):
        self._html_oss_url = value
    @property
    def html_preview_url(self):
        return self._html_preview_url

    @html_preview_url.setter
    def html_preview_url(self, value):
        self._html_preview_url = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def oss_url(self):
        return self._oss_url

    @oss_url.setter
    def oss_url(self, value):
        self._oss_url = value
    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.html_oss_url:
            if hasattr(self.html_oss_url, 'to_alipay_dict'):
                params['html_oss_url'] = self.html_oss_url.to_alipay_dict()
            else:
                params['html_oss_url'] = self.html_oss_url
        if self.html_preview_url:
            if hasattr(self.html_preview_url, 'to_alipay_dict'):
                params['html_preview_url'] = self.html_preview_url.to_alipay_dict()
            else:
                params['html_preview_url'] = self.html_preview_url
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.oss_url:
            if hasattr(self.oss_url, 'to_alipay_dict'):
                params['oss_url'] = self.oss_url.to_alipay_dict()
            else:
                params['oss_url'] = self.oss_url
        if self.preview_url:
            if hasattr(self.preview_url, 'to_alipay_dict'):
                params['preview_url'] = self.preview_url.to_alipay_dict()
            else:
                params['preview_url'] = self.preview_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateInstDTO()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'html_oss_url' in d:
            o.html_oss_url = d['html_oss_url']
        if 'html_preview_url' in d:
            o.html_preview_url = d['html_preview_url']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'oss_url' in d:
            o.oss_url = d['oss_url']
        if 'preview_url' in d:
            o.preview_url = d['preview_url']
        return o


