#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateStyleInfoDTO import TemplateStyleInfoDTO


class McardTemplate(object):

    def __init__(self):
        self._card_type = None
        self._gmt_create = None
        self._gmt_modified = None
        self._template_id = None
        self._template_style_info = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
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
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_style_info(self):
        return self._template_style_info

    @template_style_info.setter
    def template_style_info(self, value):
        if isinstance(value, TemplateStyleInfoDTO):
            self._template_style_info = value
        else:
            self._template_style_info = TemplateStyleInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
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
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_style_info:
            if hasattr(self.template_style_info, 'to_alipay_dict'):
                params['template_style_info'] = self.template_style_info.to_alipay_dict()
            else:
                params['template_style_info'] = self.template_style_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McardTemplate()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_style_info' in d:
            o.template_style_info = d['template_style_info']
        return o


