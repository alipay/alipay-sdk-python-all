#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoAssistantPresetquestionConsultModel(object):

    def __init__(self):
        self._ask_time = None
        self._customer_id = None
        self._question_content = None
        self._question_id = None
        self._scene_type = None
        self._session_id = None
        self._source_id = None

    @property
    def ask_time(self):
        return self._ask_time

    @ask_time.setter
    def ask_time(self, value):
        self._ask_time = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
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
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ask_time:
            if hasattr(self.ask_time, 'to_alipay_dict'):
                params['ask_time'] = self.ask_time.to_alipay_dict()
            else:
                params['ask_time'] = self.ask_time
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
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
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAssistantPresetquestionConsultModel()
        if 'ask_time' in d:
            o.ask_time = d['ask_time']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'question_content' in d:
            o.question_content = d['question_content']
        if 'question_id' in d:
            o.question_id = d['question_id']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


