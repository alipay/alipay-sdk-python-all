#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateElementLinkDTO(object):

    def __init__(self):
        self._content = None
        self._creator_name = None
        self._creator_no = None
        self._element_code = None
        self._name = None
        self._sort_value = None
        self._template_code = None
        self._template_version = None
        self._tenant = None
        self._type = None
        self._uk = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def creator_name(self):
        return self._creator_name

    @creator_name.setter
    def creator_name(self, value):
        self._creator_name = value
    @property
    def creator_no(self):
        return self._creator_no

    @creator_no.setter
    def creator_no(self, value):
        self._creator_no = value
    @property
    def element_code(self):
        return self._element_code

    @element_code.setter
    def element_code(self, value):
        self._element_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sort_value(self):
        return self._sort_value

    @sort_value.setter
    def sort_value(self, value):
        self._sort_value = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def uk(self):
        return self._uk

    @uk.setter
    def uk(self, value):
        self._uk = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.creator_name:
            if hasattr(self.creator_name, 'to_alipay_dict'):
                params['creator_name'] = self.creator_name.to_alipay_dict()
            else:
                params['creator_name'] = self.creator_name
        if self.creator_no:
            if hasattr(self.creator_no, 'to_alipay_dict'):
                params['creator_no'] = self.creator_no.to_alipay_dict()
            else:
                params['creator_no'] = self.creator_no
        if self.element_code:
            if hasattr(self.element_code, 'to_alipay_dict'):
                params['element_code'] = self.element_code.to_alipay_dict()
            else:
                params['element_code'] = self.element_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.sort_value:
            if hasattr(self.sort_value, 'to_alipay_dict'):
                params['sort_value'] = self.sort_value.to_alipay_dict()
            else:
                params['sort_value'] = self.sort_value
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_version:
            if hasattr(self.template_version, 'to_alipay_dict'):
                params['template_version'] = self.template_version.to_alipay_dict()
            else:
                params['template_version'] = self.template_version
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.uk:
            if hasattr(self.uk, 'to_alipay_dict'):
                params['uk'] = self.uk.to_alipay_dict()
            else:
                params['uk'] = self.uk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateElementLinkDTO()
        if 'content' in d:
            o.content = d['content']
        if 'creator_name' in d:
            o.creator_name = d['creator_name']
        if 'creator_no' in d:
            o.creator_no = d['creator_no']
        if 'element_code' in d:
            o.element_code = d['element_code']
        if 'name' in d:
            o.name = d['name']
        if 'sort_value' in d:
            o.sort_value = d['sort_value']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_version' in d:
            o.template_version = d['template_version']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'type' in d:
            o.type = d['type']
        if 'uk' in d:
            o.uk = d['uk']
        return o


