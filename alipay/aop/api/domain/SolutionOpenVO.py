#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SolutionAttributeInfoOpenVO import SolutionAttributeInfoOpenVO
from alipay.aop.api.domain.ContractTemplateOpenVO import ContractTemplateOpenVO


class SolutionOpenVO(object):

    def __init__(self):
        self._attribute_vo_list = None
        self._extend_mode = None
        self._gmt_create = None
        self._gmt_modified = None
        self._solution_code = None
        self._solution_desc = None
        self._solution_name = None
        self._template_list = None

    @property
    def attribute_vo_list(self):
        return self._attribute_vo_list

    @attribute_vo_list.setter
    def attribute_vo_list(self, value):
        if isinstance(value, list):
            self._attribute_vo_list = list()
            for i in value:
                if isinstance(i, SolutionAttributeInfoOpenVO):
                    self._attribute_vo_list.append(i)
                else:
                    self._attribute_vo_list.append(SolutionAttributeInfoOpenVO.from_alipay_dict(i))
    @property
    def extend_mode(self):
        return self._extend_mode

    @extend_mode.setter
    def extend_mode(self, value):
        self._extend_mode = value
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
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def solution_desc(self):
        return self._solution_desc

    @solution_desc.setter
    def solution_desc(self, value):
        self._solution_desc = value
    @property
    def solution_name(self):
        return self._solution_name

    @solution_name.setter
    def solution_name(self, value):
        self._solution_name = value
    @property
    def template_list(self):
        return self._template_list

    @template_list.setter
    def template_list(self, value):
        if isinstance(value, list):
            self._template_list = list()
            for i in value:
                if isinstance(i, ContractTemplateOpenVO):
                    self._template_list.append(i)
                else:
                    self._template_list.append(ContractTemplateOpenVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.attribute_vo_list:
            if isinstance(self.attribute_vo_list, list):
                for i in range(0, len(self.attribute_vo_list)):
                    element = self.attribute_vo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attribute_vo_list[i] = element.to_alipay_dict()
            if hasattr(self.attribute_vo_list, 'to_alipay_dict'):
                params['attribute_vo_list'] = self.attribute_vo_list.to_alipay_dict()
            else:
                params['attribute_vo_list'] = self.attribute_vo_list
        if self.extend_mode:
            if hasattr(self.extend_mode, 'to_alipay_dict'):
                params['extend_mode'] = self.extend_mode.to_alipay_dict()
            else:
                params['extend_mode'] = self.extend_mode
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
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.solution_desc:
            if hasattr(self.solution_desc, 'to_alipay_dict'):
                params['solution_desc'] = self.solution_desc.to_alipay_dict()
            else:
                params['solution_desc'] = self.solution_desc
        if self.solution_name:
            if hasattr(self.solution_name, 'to_alipay_dict'):
                params['solution_name'] = self.solution_name.to_alipay_dict()
            else:
                params['solution_name'] = self.solution_name
        if self.template_list:
            if isinstance(self.template_list, list):
                for i in range(0, len(self.template_list)):
                    element = self.template_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_list[i] = element.to_alipay_dict()
            if hasattr(self.template_list, 'to_alipay_dict'):
                params['template_list'] = self.template_list.to_alipay_dict()
            else:
                params['template_list'] = self.template_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SolutionOpenVO()
        if 'attribute_vo_list' in d:
            o.attribute_vo_list = d['attribute_vo_list']
        if 'extend_mode' in d:
            o.extend_mode = d['extend_mode']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'solution_desc' in d:
            o.solution_desc = d['solution_desc']
        if 'solution_name' in d:
            o.solution_name = d['solution_name']
        if 'template_list' in d:
            o.template_list = d['template_list']
        return o


