#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DialogueKeyWord import DialogueKeyWord


class HitDialogue(object):

    def __init__(self):
        self._key_words = None
        self._pid = None

    @property
    def key_words(self):
        return self._key_words

    @key_words.setter
    def key_words(self, value):
        if isinstance(value, list):
            self._key_words = list()
            for i in value:
                if isinstance(i, DialogueKeyWord):
                    self._key_words.append(i)
                else:
                    self._key_words.append(DialogueKeyWord.from_alipay_dict(i))
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.key_words:
            if isinstance(self.key_words, list):
                for i in range(0, len(self.key_words)):
                    element = self.key_words[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_words[i] = element.to_alipay_dict()
            if hasattr(self.key_words, 'to_alipay_dict'):
                params['key_words'] = self.key_words.to_alipay_dict()
            else:
                params['key_words'] = self.key_words
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HitDialogue()
        if 'key_words' in d:
            o.key_words = d['key_words']
        if 'pid' in d:
            o.pid = d['pid']
        return o


