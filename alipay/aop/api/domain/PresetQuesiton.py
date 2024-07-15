#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PresetQuesiton(object):

    def __init__(self):
        self._parent_id = None
        self._question_content = None
        self._question_id = None
        self._question_type = None

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def question_content(self):
        return self._question_content

    @question_content.setter
    def question_content(self, value):
        self._question_content = value
    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, value):
        self._question_id = value
    @property
    def question_type(self):
        return self._question_type

    @question_type.setter
    def question_type(self, value):
        self._question_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.question_content:
            if hasattr(self.question_content, 'to_alipay_dict'):
                params['question_content'] = self.question_content.to_alipay_dict()
            else:
                params['question_content'] = self.question_content
        if self.question_id:
            if hasattr(self.question_id, 'to_alipay_dict'):
                params['question_id'] = self.question_id.to_alipay_dict()
            else:
                params['question_id'] = self.question_id
        if self.question_type:
            if hasattr(self.question_type, 'to_alipay_dict'):
                params['question_type'] = self.question_type.to_alipay_dict()
            else:
                params['question_type'] = self.question_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PresetQuesiton()
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'question_content' in d:
            o.question_content = d['question_content']
        if 'question_id' in d:
            o.question_id = d['question_id']
        if 'question_type' in d:
            o.question_type = d['question_type']
        return o


