#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateDataDTO import TemplateDataDTO


class ChatContentDTO(object):

    def __init__(self):
        self._index = None
        self._template_data = None
        self._template_id = None
        self._template_type = None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def template_data(self):
        return self._template_data

    @template_data.setter
    def template_data(self, value):
        if isinstance(value, TemplateDataDTO):
            self._template_data = value
        else:
            self._template_data = TemplateDataDTO.from_alipay_dict(value)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.template_data:
            if hasattr(self.template_data, 'to_alipay_dict'):
                params['template_data'] = self.template_data.to_alipay_dict()
            else:
                params['template_data'] = self.template_data
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatContentDTO()
        if 'index' in d:
            o.index = d['index']
        if 'template_data' in d:
            o.template_data = d['template_data']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_type' in d:
            o.template_type = d['template_type']
        return o


