#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateTextMessageDTO import TemplateTextMessageDTO


class TemplateOperationDTO(object):

    def __init__(self):
        self._alt_text = None
        self._format_type = None
        self._message = None
        self._message_encoding = None
        self._text_messages = None

    @property
    def alt_text(self):
        return self._alt_text

    @alt_text.setter
    def alt_text(self, value):
        self._alt_text = value
    @property
    def format_type(self):
        return self._format_type

    @format_type.setter
    def format_type(self, value):
        self._format_type = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def message_encoding(self):
        return self._message_encoding

    @message_encoding.setter
    def message_encoding(self, value):
        self._message_encoding = value
    @property
    def text_messages(self):
        return self._text_messages

    @text_messages.setter
    def text_messages(self, value):
        if isinstance(value, list):
            self._text_messages = list()
            for i in value:
                if isinstance(i, TemplateTextMessageDTO):
                    self._text_messages.append(i)
                else:
                    self._text_messages.append(TemplateTextMessageDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alt_text:
            if hasattr(self.alt_text, 'to_alipay_dict'):
                params['alt_text'] = self.alt_text.to_alipay_dict()
            else:
                params['alt_text'] = self.alt_text
        if self.format_type:
            if hasattr(self.format_type, 'to_alipay_dict'):
                params['format_type'] = self.format_type.to_alipay_dict()
            else:
                params['format_type'] = self.format_type
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.message_encoding:
            if hasattr(self.message_encoding, 'to_alipay_dict'):
                params['message_encoding'] = self.message_encoding.to_alipay_dict()
            else:
                params['message_encoding'] = self.message_encoding
        if self.text_messages:
            if isinstance(self.text_messages, list):
                for i in range(0, len(self.text_messages)):
                    element = self.text_messages[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.text_messages[i] = element.to_alipay_dict()
            if hasattr(self.text_messages, 'to_alipay_dict'):
                params['text_messages'] = self.text_messages.to_alipay_dict()
            else:
                params['text_messages'] = self.text_messages
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateOperationDTO()
        if 'alt_text' in d:
            o.alt_text = d['alt_text']
        if 'format_type' in d:
            o.format_type = d['format_type']
        if 'message' in d:
            o.message = d['message']
        if 'message_encoding' in d:
            o.message_encoding = d['message_encoding']
        if 'text_messages' in d:
            o.text_messages = d['text_messages']
        return o


