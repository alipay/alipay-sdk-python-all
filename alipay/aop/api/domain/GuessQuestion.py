#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GuessQuestion(object):

    def __init__(self):
        self._question_content = None
        self._question_id = None
        self._question_type = None
        self._scene_type = None

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
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GuessQuestion()
        if 'question_content' in d:
            o.question_content = d['question_content']
        if 'question_id' in d:
            o.question_id = d['question_id']
        if 'question_type' in d:
            o.question_type = d['question_type']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


