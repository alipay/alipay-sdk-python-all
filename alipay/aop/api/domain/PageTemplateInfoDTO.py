#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PageTemplateParamInfoDTO import PageTemplateParamInfoDTO


class PageTemplateInfoDTO(object):

    def __init__(self):
        self._code = None
        self._creator_id = None
        self._creator_name = None
        self._current_version = None
        self._edit_version = None
        self._gmt_create = None
        self._gmt_create_code = None
        self._gmt_modified = None
        self._id = None
        self._modifier_id = None
        self._modifier_name = None
        self._name = None
        self._param_template_list = None
        self._picture_url = None
        self._preview_url = None
        self._resolve_code = None
        self._run_version = None
        self._type = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def creator_name(self):
        return self._creator_name

    @creator_name.setter
    def creator_name(self, value):
        self._creator_name = value
    @property
    def current_version(self):
        return self._current_version

    @current_version.setter
    def current_version(self, value):
        self._current_version = value
    @property
    def edit_version(self):
        return self._edit_version

    @edit_version.setter
    def edit_version(self, value):
        self._edit_version = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_create_code(self):
        return self._gmt_create_code

    @gmt_create_code.setter
    def gmt_create_code(self, value):
        self._gmt_create_code = value
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
    def modifier_id(self):
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, value):
        self._modifier_id = value
    @property
    def modifier_name(self):
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, value):
        self._modifier_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def param_template_list(self):
        return self._param_template_list

    @param_template_list.setter
    def param_template_list(self, value):
        if isinstance(value, list):
            self._param_template_list = list()
            for i in value:
                if isinstance(i, PageTemplateParamInfoDTO):
                    self._param_template_list.append(i)
                else:
                    self._param_template_list.append(PageTemplateParamInfoDTO.from_alipay_dict(i))
    @property
    def picture_url(self):
        return self._picture_url

    @picture_url.setter
    def picture_url(self, value):
        self._picture_url = value
    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value
    @property
    def resolve_code(self):
        return self._resolve_code

    @resolve_code.setter
    def resolve_code(self, value):
        self._resolve_code = value
    @property
    def run_version(self):
        return self._run_version

    @run_version.setter
    def run_version(self, value):
        self._run_version = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.creator_name:
            if hasattr(self.creator_name, 'to_alipay_dict'):
                params['creator_name'] = self.creator_name.to_alipay_dict()
            else:
                params['creator_name'] = self.creator_name
        if self.current_version:
            if hasattr(self.current_version, 'to_alipay_dict'):
                params['current_version'] = self.current_version.to_alipay_dict()
            else:
                params['current_version'] = self.current_version
        if self.edit_version:
            if hasattr(self.edit_version, 'to_alipay_dict'):
                params['edit_version'] = self.edit_version.to_alipay_dict()
            else:
                params['edit_version'] = self.edit_version
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_create_code:
            if hasattr(self.gmt_create_code, 'to_alipay_dict'):
                params['gmt_create_code'] = self.gmt_create_code.to_alipay_dict()
            else:
                params['gmt_create_code'] = self.gmt_create_code
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
        if self.modifier_id:
            if hasattr(self.modifier_id, 'to_alipay_dict'):
                params['modifier_id'] = self.modifier_id.to_alipay_dict()
            else:
                params['modifier_id'] = self.modifier_id
        if self.modifier_name:
            if hasattr(self.modifier_name, 'to_alipay_dict'):
                params['modifier_name'] = self.modifier_name.to_alipay_dict()
            else:
                params['modifier_name'] = self.modifier_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.param_template_list:
            if isinstance(self.param_template_list, list):
                for i in range(0, len(self.param_template_list)):
                    element = self.param_template_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.param_template_list[i] = element.to_alipay_dict()
            if hasattr(self.param_template_list, 'to_alipay_dict'):
                params['param_template_list'] = self.param_template_list.to_alipay_dict()
            else:
                params['param_template_list'] = self.param_template_list
        if self.picture_url:
            if hasattr(self.picture_url, 'to_alipay_dict'):
                params['picture_url'] = self.picture_url.to_alipay_dict()
            else:
                params['picture_url'] = self.picture_url
        if self.preview_url:
            if hasattr(self.preview_url, 'to_alipay_dict'):
                params['preview_url'] = self.preview_url.to_alipay_dict()
            else:
                params['preview_url'] = self.preview_url
        if self.resolve_code:
            if hasattr(self.resolve_code, 'to_alipay_dict'):
                params['resolve_code'] = self.resolve_code.to_alipay_dict()
            else:
                params['resolve_code'] = self.resolve_code
        if self.run_version:
            if hasattr(self.run_version, 'to_alipay_dict'):
                params['run_version'] = self.run_version.to_alipay_dict()
            else:
                params['run_version'] = self.run_version
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PageTemplateInfoDTO()
        if 'code' in d:
            o.code = d['code']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'creator_name' in d:
            o.creator_name = d['creator_name']
        if 'current_version' in d:
            o.current_version = d['current_version']
        if 'edit_version' in d:
            o.edit_version = d['edit_version']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_create_code' in d:
            o.gmt_create_code = d['gmt_create_code']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'modifier_id' in d:
            o.modifier_id = d['modifier_id']
        if 'modifier_name' in d:
            o.modifier_name = d['modifier_name']
        if 'name' in d:
            o.name = d['name']
        if 'param_template_list' in d:
            o.param_template_list = d['param_template_list']
        if 'picture_url' in d:
            o.picture_url = d['picture_url']
        if 'preview_url' in d:
            o.preview_url = d['preview_url']
        if 'resolve_code' in d:
            o.resolve_code = d['resolve_code']
        if 'run_version' in d:
            o.run_version = d['run_version']
        if 'type' in d:
            o.type = d['type']
        return o


