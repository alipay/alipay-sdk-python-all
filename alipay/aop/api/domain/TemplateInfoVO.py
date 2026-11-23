#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateInfoVO(object):

    def __init__(self):
        self._intro_url = None
        self._template_code = None
        self._template_desc = None
        self._template_md = None
        self._template_name = None
        self._template_version = None

    @property
    def intro_url(self):
        return self._intro_url

    @intro_url.setter
    def intro_url(self, value):
        self._intro_url = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_desc(self):
        return self._template_desc

    @template_desc.setter
    def template_desc(self, value):
        self._template_desc = value
    @property
    def template_md(self):
        return self._template_md

    @template_md.setter
    def template_md(self, value):
        self._template_md = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.intro_url:
            if hasattr(self.intro_url, 'to_alipay_dict'):
                params['intro_url'] = self.intro_url.to_alipay_dict()
            else:
                params['intro_url'] = self.intro_url
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_desc:
            if hasattr(self.template_desc, 'to_alipay_dict'):
                params['template_desc'] = self.template_desc.to_alipay_dict()
            else:
                params['template_desc'] = self.template_desc
        if self.template_md:
            if hasattr(self.template_md, 'to_alipay_dict'):
                params['template_md'] = self.template_md.to_alipay_dict()
            else:
                params['template_md'] = self.template_md
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.template_version:
            if hasattr(self.template_version, 'to_alipay_dict'):
                params['template_version'] = self.template_version.to_alipay_dict()
            else:
                params['template_version'] = self.template_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateInfoVO()
        if 'intro_url' in d:
            o.intro_url = d['intro_url']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_desc' in d:
            o.template_desc = d['template_desc']
        if 'template_md' in d:
            o.template_md = d['template_md']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'template_version' in d:
            o.template_version = d['template_version']
        return o


