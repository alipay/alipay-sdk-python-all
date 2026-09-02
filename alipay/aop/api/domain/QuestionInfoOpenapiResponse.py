#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OptionItemResponse import OptionItemResponse


class QuestionInfoOpenapiResponse(object):

    def __init__(self):
        self._input_type = None
        self._options = None
        self._question_biz_id = None
        self._question_category = None
        self._question_content = None
        self._question_desc = None
        self._question_sort_order = None
        self._required = None

    @property
    def input_type(self):
        return self._input_type

    @input_type.setter
    def input_type(self, value):
        self._input_type = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, OptionItemResponse):
                    self._options.append(i)
                else:
                    self._options.append(OptionItemResponse.from_alipay_dict(i))
    @property
    def question_biz_id(self):
        return self._question_biz_id

    @question_biz_id.setter
    def question_biz_id(self, value):
        self._question_biz_id = value
    @property
    def question_category(self):
        return self._question_category

    @question_category.setter
    def question_category(self, value):
        self._question_category = value
    @property
    def question_content(self):
        return self._question_content

    @question_content.setter
    def question_content(self, value):
        self._question_content = value
    @property
    def question_desc(self):
        return self._question_desc

    @question_desc.setter
    def question_desc(self, value):
        self._question_desc = value
    @property
    def question_sort_order(self):
        return self._question_sort_order

    @question_sort_order.setter
    def question_sort_order(self, value):
        self._question_sort_order = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_type:
            if hasattr(self.input_type, 'to_alipay_dict'):
                params['input_type'] = self.input_type.to_alipay_dict()
            else:
                params['input_type'] = self.input_type
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.question_biz_id:
            if hasattr(self.question_biz_id, 'to_alipay_dict'):
                params['question_biz_id'] = self.question_biz_id.to_alipay_dict()
            else:
                params['question_biz_id'] = self.question_biz_id
        if self.question_category:
            if hasattr(self.question_category, 'to_alipay_dict'):
                params['question_category'] = self.question_category.to_alipay_dict()
            else:
                params['question_category'] = self.question_category
        if self.question_content:
            if hasattr(self.question_content, 'to_alipay_dict'):
                params['question_content'] = self.question_content.to_alipay_dict()
            else:
                params['question_content'] = self.question_content
        if self.question_desc:
            if hasattr(self.question_desc, 'to_alipay_dict'):
                params['question_desc'] = self.question_desc.to_alipay_dict()
            else:
                params['question_desc'] = self.question_desc
        if self.question_sort_order:
            if hasattr(self.question_sort_order, 'to_alipay_dict'):
                params['question_sort_order'] = self.question_sort_order.to_alipay_dict()
            else:
                params['question_sort_order'] = self.question_sort_order
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuestionInfoOpenapiResponse()
        if 'input_type' in d:
            o.input_type = d['input_type']
        if 'options' in d:
            o.options = d['options']
        if 'question_biz_id' in d:
            o.question_biz_id = d['question_biz_id']
        if 'question_category' in d:
            o.question_category = d['question_category']
        if 'question_content' in d:
            o.question_content = d['question_content']
        if 'question_desc' in d:
            o.question_desc = d['question_desc']
        if 'question_sort_order' in d:
            o.question_sort_order = d['question_sort_order']
        if 'required' in d:
            o.required = d['required']
        return o


