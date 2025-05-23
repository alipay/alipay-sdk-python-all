#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreativeTemplateDetailRes import CreativeTemplateDetailRes
from alipay.aop.api.domain.CreativeTemplateDetailRes import CreativeTemplateDetailRes
from alipay.aop.api.domain.CreativeTemplateDetailRes import CreativeTemplateDetailRes


class CreativeTemplateResp(object):

    def __init__(self):
        self._desc_template_detail = None
        self._material_template_detail = None
        self._template_desc = None
        self._template_id = None
        self._template_name = None
        self._title_template_detail = None

    @property
    def desc_template_detail(self):
        return self._desc_template_detail

    @desc_template_detail.setter
    def desc_template_detail(self, value):
        if isinstance(value, list):
            self._desc_template_detail = list()
            for i in value:
                if isinstance(i, CreativeTemplateDetailRes):
                    self._desc_template_detail.append(i)
                else:
                    self._desc_template_detail.append(CreativeTemplateDetailRes.from_alipay_dict(i))
    @property
    def material_template_detail(self):
        return self._material_template_detail

    @material_template_detail.setter
    def material_template_detail(self, value):
        if isinstance(value, list):
            self._material_template_detail = list()
            for i in value:
                if isinstance(i, CreativeTemplateDetailRes):
                    self._material_template_detail.append(i)
                else:
                    self._material_template_detail.append(CreativeTemplateDetailRes.from_alipay_dict(i))
    @property
    def template_desc(self):
        return self._template_desc

    @template_desc.setter
    def template_desc(self, value):
        self._template_desc = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def title_template_detail(self):
        return self._title_template_detail

    @title_template_detail.setter
    def title_template_detail(self, value):
        if isinstance(value, list):
            self._title_template_detail = list()
            for i in value:
                if isinstance(i, CreativeTemplateDetailRes):
                    self._title_template_detail.append(i)
                else:
                    self._title_template_detail.append(CreativeTemplateDetailRes.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.desc_template_detail:
            if isinstance(self.desc_template_detail, list):
                for i in range(0, len(self.desc_template_detail)):
                    element = self.desc_template_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.desc_template_detail[i] = element.to_alipay_dict()
            if hasattr(self.desc_template_detail, 'to_alipay_dict'):
                params['desc_template_detail'] = self.desc_template_detail.to_alipay_dict()
            else:
                params['desc_template_detail'] = self.desc_template_detail
        if self.material_template_detail:
            if isinstance(self.material_template_detail, list):
                for i in range(0, len(self.material_template_detail)):
                    element = self.material_template_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_template_detail[i] = element.to_alipay_dict()
            if hasattr(self.material_template_detail, 'to_alipay_dict'):
                params['material_template_detail'] = self.material_template_detail.to_alipay_dict()
            else:
                params['material_template_detail'] = self.material_template_detail
        if self.template_desc:
            if hasattr(self.template_desc, 'to_alipay_dict'):
                params['template_desc'] = self.template_desc.to_alipay_dict()
            else:
                params['template_desc'] = self.template_desc
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.title_template_detail:
            if isinstance(self.title_template_detail, list):
                for i in range(0, len(self.title_template_detail)):
                    element = self.title_template_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.title_template_detail[i] = element.to_alipay_dict()
            if hasattr(self.title_template_detail, 'to_alipay_dict'):
                params['title_template_detail'] = self.title_template_detail.to_alipay_dict()
            else:
                params['title_template_detail'] = self.title_template_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeTemplateResp()
        if 'desc_template_detail' in d:
            o.desc_template_detail = d['desc_template_detail']
        if 'material_template_detail' in d:
            o.material_template_detail = d['material_template_detail']
        if 'template_desc' in d:
            o.template_desc = d['template_desc']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'title_template_detail' in d:
            o.title_template_detail = d['title_template_detail']
        return o


