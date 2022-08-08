#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FormTemplateRelationDTO(object):

    def __init__(self):
        self._form_template_id = None
        self._form_template_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._marketing_type = None

    @property
    def form_template_id(self):
        return self._form_template_id

    @form_template_id.setter
    def form_template_id(self, value):
        self._form_template_id = value
    @property
    def form_template_name(self):
        return self._form_template_name

    @form_template_name.setter
    def form_template_name(self, value):
        self._form_template_name = value
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
    def marketing_type(self):
        return self._marketing_type

    @marketing_type.setter
    def marketing_type(self, value):
        self._marketing_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.form_template_id:
            if hasattr(self.form_template_id, 'to_alipay_dict'):
                params['form_template_id'] = self.form_template_id.to_alipay_dict()
            else:
                params['form_template_id'] = self.form_template_id
        if self.form_template_name:
            if hasattr(self.form_template_name, 'to_alipay_dict'):
                params['form_template_name'] = self.form_template_name.to_alipay_dict()
            else:
                params['form_template_name'] = self.form_template_name
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
        if self.marketing_type:
            if hasattr(self.marketing_type, 'to_alipay_dict'):
                params['marketing_type'] = self.marketing_type.to_alipay_dict()
            else:
                params['marketing_type'] = self.marketing_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FormTemplateRelationDTO()
        if 'form_template_id' in d:
            o.form_template_id = d['form_template_id']
        if 'form_template_name' in d:
            o.form_template_name = d['form_template_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'marketing_type' in d:
            o.marketing_type = d['marketing_type']
        return o


