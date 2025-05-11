#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateContent import TemplateContent


class OpenChatContent(object):

    def __init__(self):
        self._pack_no = None
        self._step = None
        self._template = None
        self._text = None
        self._time = None
        self._title = None
        self._tpl_code = None
        self._tpl_data = None
        self._type = None

    @property
    def pack_no(self):
        return self._pack_no

    @pack_no.setter
    def pack_no(self, value):
        self._pack_no = value
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        if isinstance(value, TemplateContent):
            self._template = value
        else:
            self._template = TemplateContent.from_alipay_dict(value)
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def tpl_code(self):
        return self._tpl_code

    @tpl_code.setter
    def tpl_code(self, value):
        self._tpl_code = value
    @property
    def tpl_data(self):
        return self._tpl_data

    @tpl_data.setter
    def tpl_data(self, value):
        self._tpl_data = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.pack_no:
            if hasattr(self.pack_no, 'to_alipay_dict'):
                params['pack_no'] = self.pack_no.to_alipay_dict()
            else:
                params['pack_no'] = self.pack_no
        if self.step:
            if hasattr(self.step, 'to_alipay_dict'):
                params['step'] = self.step.to_alipay_dict()
            else:
                params['step'] = self.step
        if self.template:
            if hasattr(self.template, 'to_alipay_dict'):
                params['template'] = self.template.to_alipay_dict()
            else:
                params['template'] = self.template
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.tpl_code:
            if hasattr(self.tpl_code, 'to_alipay_dict'):
                params['tpl_code'] = self.tpl_code.to_alipay_dict()
            else:
                params['tpl_code'] = self.tpl_code
        if self.tpl_data:
            if hasattr(self.tpl_data, 'to_alipay_dict'):
                params['tpl_data'] = self.tpl_data.to_alipay_dict()
            else:
                params['tpl_data'] = self.tpl_data
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
        o = OpenChatContent()
        if 'pack_no' in d:
            o.pack_no = d['pack_no']
        if 'step' in d:
            o.step = d['step']
        if 'template' in d:
            o.template = d['template']
        if 'text' in d:
            o.text = d['text']
        if 'time' in d:
            o.time = d['time']
        if 'title' in d:
            o.title = d['title']
        if 'tpl_code' in d:
            o.tpl_code = d['tpl_code']
        if 'tpl_data' in d:
            o.tpl_data = d['tpl_data']
        if 'type' in d:
            o.type = d['type']
        return o


