#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StreamContent(object):

    def __init__(self):
        self._reply_cmd = None
        self._stream_type = None
        self._template_code = None
        self._template_data = None
        self._text = None

    @property
    def reply_cmd(self):
        return self._reply_cmd

    @reply_cmd.setter
    def reply_cmd(self, value):
        self._reply_cmd = value
    @property
    def stream_type(self):
        return self._stream_type

    @stream_type.setter
    def stream_type(self, value):
        self._stream_type = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_data(self):
        return self._template_data

    @template_data.setter
    def template_data(self, value):
        self._template_data = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.reply_cmd:
            if hasattr(self.reply_cmd, 'to_alipay_dict'):
                params['reply_cmd'] = self.reply_cmd.to_alipay_dict()
            else:
                params['reply_cmd'] = self.reply_cmd
        if self.stream_type:
            if hasattr(self.stream_type, 'to_alipay_dict'):
                params['stream_type'] = self.stream_type.to_alipay_dict()
            else:
                params['stream_type'] = self.stream_type
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_data:
            if hasattr(self.template_data, 'to_alipay_dict'):
                params['template_data'] = self.template_data.to_alipay_dict()
            else:
                params['template_data'] = self.template_data
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StreamContent()
        if 'reply_cmd' in d:
            o.reply_cmd = d['reply_cmd']
        if 'stream_type' in d:
            o.stream_type = d['stream_type']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_data' in d:
            o.template_data = d['template_data']
        if 'text' in d:
            o.text = d['text']
        return o


