#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpiDetectionDetail(object):

    def __init__(self):
        self._code = None
        self._content = None
        self._data_id = None
        self._details = None
        self._label = None
        self._msg = None
        self._rate = None
        self._scene = None
        self._suggestion = None
        self._task_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                self._details.append(i)
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.details:
            if isinstance(self.details, list):
                for i in range(0, len(self.details)):
                    element = self.details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.details[i] = element.to_alipay_dict()
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.suggestion:
            if hasattr(self.suggestion, 'to_alipay_dict'):
                params['suggestion'] = self.suggestion.to_alipay_dict()
            else:
                params['suggestion'] = self.suggestion
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpiDetectionDetail()
        if 'code' in d:
            o.code = d['code']
        if 'content' in d:
            o.content = d['content']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'details' in d:
            o.details = d['details']
        if 'label' in d:
            o.label = d['label']
        if 'msg' in d:
            o.msg = d['msg']
        if 'rate' in d:
            o.rate = d['rate']
        if 'scene' in d:
            o.scene = d['scene']
        if 'suggestion' in d:
            o.suggestion = d['suggestion']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


