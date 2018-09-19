#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarDialogonlineAnswerPushModel(object):

    def __init__(self):
        self._answer_content = None
        self._answer_id = None
        self._answer_logo = None
        self._answer_name = None
        self._answer_pic = None
        self._answer_time = None
        self._answer_type = None
        self._content_type = None
        self._question_id = None

    @property
    def answer_content(self):
        return self._answer_content

    @answer_content.setter
    def answer_content(self, value):
        self._answer_content = value
    @property
    def answer_id(self):
        return self._answer_id

    @answer_id.setter
    def answer_id(self, value):
        self._answer_id = value
    @property
    def answer_logo(self):
        return self._answer_logo

    @answer_logo.setter
    def answer_logo(self, value):
        self._answer_logo = value
    @property
    def answer_name(self):
        return self._answer_name

    @answer_name.setter
    def answer_name(self, value):
        self._answer_name = value
    @property
    def answer_pic(self):
        return self._answer_pic

    @answer_pic.setter
    def answer_pic(self, value):
        self._answer_pic = value
    @property
    def answer_time(self):
        return self._answer_time

    @answer_time.setter
    def answer_time(self, value):
        self._answer_time = value
    @property
    def answer_type(self):
        return self._answer_type

    @answer_type.setter
    def answer_type(self, value):
        self._answer_type = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, value):
        self._question_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer_content:
            if hasattr(self.answer_content, 'to_alipay_dict'):
                params['answer_content'] = self.answer_content.to_alipay_dict()
            else:
                params['answer_content'] = self.answer_content
        if self.answer_id:
            if hasattr(self.answer_id, 'to_alipay_dict'):
                params['answer_id'] = self.answer_id.to_alipay_dict()
            else:
                params['answer_id'] = self.answer_id
        if self.answer_logo:
            if hasattr(self.answer_logo, 'to_alipay_dict'):
                params['answer_logo'] = self.answer_logo.to_alipay_dict()
            else:
                params['answer_logo'] = self.answer_logo
        if self.answer_name:
            if hasattr(self.answer_name, 'to_alipay_dict'):
                params['answer_name'] = self.answer_name.to_alipay_dict()
            else:
                params['answer_name'] = self.answer_name
        if self.answer_pic:
            if hasattr(self.answer_pic, 'to_alipay_dict'):
                params['answer_pic'] = self.answer_pic.to_alipay_dict()
            else:
                params['answer_pic'] = self.answer_pic
        if self.answer_time:
            if hasattr(self.answer_time, 'to_alipay_dict'):
                params['answer_time'] = self.answer_time.to_alipay_dict()
            else:
                params['answer_time'] = self.answer_time
        if self.answer_type:
            if hasattr(self.answer_type, 'to_alipay_dict'):
                params['answer_type'] = self.answer_type.to_alipay_dict()
            else:
                params['answer_type'] = self.answer_type
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.question_id:
            if hasattr(self.question_id, 'to_alipay_dict'):
                params['question_id'] = self.question_id.to_alipay_dict()
            else:
                params['question_id'] = self.question_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarDialogonlineAnswerPushModel()
        if 'answer_content' in d:
            o.answer_content = d['answer_content']
        if 'answer_id' in d:
            o.answer_id = d['answer_id']
        if 'answer_logo' in d:
            o.answer_logo = d['answer_logo']
        if 'answer_name' in d:
            o.answer_name = d['answer_name']
        if 'answer_pic' in d:
            o.answer_pic = d['answer_pic']
        if 'answer_time' in d:
            o.answer_time = d['answer_time']
        if 'answer_type' in d:
            o.answer_type = d['answer_type']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'question_id' in d:
            o.question_id = d['question_id']
        return o


