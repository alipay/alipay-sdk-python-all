#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TagOptionCategoryOpenDetail import TagOptionCategoryOpenDetail


class SelectTagOptionOpenCategory(object):

    def __init__(self):
        self._options = None
        self._tag_option_category_id = None
        self._tag_option_category_name = None
        self._type = None

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, TagOptionCategoryOpenDetail):
            self._options = value
        else:
            self._options = TagOptionCategoryOpenDetail.from_alipay_dict(value)
    @property
    def tag_option_category_id(self):
        return self._tag_option_category_id

    @tag_option_category_id.setter
    def tag_option_category_id(self, value):
        self._tag_option_category_id = value
    @property
    def tag_option_category_name(self):
        return self._tag_option_category_name

    @tag_option_category_name.setter
    def tag_option_category_name(self, value):
        self._tag_option_category_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.options:
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.tag_option_category_id:
            if hasattr(self.tag_option_category_id, 'to_alipay_dict'):
                params['tag_option_category_id'] = self.tag_option_category_id.to_alipay_dict()
            else:
                params['tag_option_category_id'] = self.tag_option_category_id
        if self.tag_option_category_name:
            if hasattr(self.tag_option_category_name, 'to_alipay_dict'):
                params['tag_option_category_name'] = self.tag_option_category_name.to_alipay_dict()
            else:
                params['tag_option_category_name'] = self.tag_option_category_name
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
        o = SelectTagOptionOpenCategory()
        if 'options' in d:
            o.options = d['options']
        if 'tag_option_category_id' in d:
            o.tag_option_category_id = d['tag_option_category_id']
        if 'tag_option_category_name' in d:
            o.tag_option_category_name = d['tag_option_category_name']
        if 'type' in d:
            o.type = d['type']
        return o


