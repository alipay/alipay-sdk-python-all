#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TextLanguageReq import TextLanguageReq


class CommonTextReq(object):

    def __init__(self):
        self._language_list = None
        self._note = None
        self._tag_list = None
        self._text_key = None

    @property
    def language_list(self):
        return self._language_list

    @language_list.setter
    def language_list(self, value):
        if isinstance(value, list):
            self._language_list = list()
            for i in value:
                if isinstance(i, TextLanguageReq):
                    self._language_list.append(i)
                else:
                    self._language_list.append(TextLanguageReq.from_alipay_dict(i))
    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                self._tag_list.append(i)
    @property
    def text_key(self):
        return self._text_key

    @text_key.setter
    def text_key(self, value):
        self._text_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.language_list:
            if isinstance(self.language_list, list):
                for i in range(0, len(self.language_list)):
                    element = self.language_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.language_list[i] = element.to_alipay_dict()
            if hasattr(self.language_list, 'to_alipay_dict'):
                params['language_list'] = self.language_list.to_alipay_dict()
            else:
                params['language_list'] = self.language_list
        if self.note:
            if hasattr(self.note, 'to_alipay_dict'):
                params['note'] = self.note.to_alipay_dict()
            else:
                params['note'] = self.note
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        if self.text_key:
            if hasattr(self.text_key, 'to_alipay_dict'):
                params['text_key'] = self.text_key.to_alipay_dict()
            else:
                params['text_key'] = self.text_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonTextReq()
        if 'language_list' in d:
            o.language_list = d['language_list']
        if 'note' in d:
            o.note = d['note']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'text_key' in d:
            o.text_key = d['text_key']
        return o


