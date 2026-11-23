#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HittedRule(object):

    def __init__(self):
        self._hit_words = None
        self._level = None
        self._result_tips = None
        self._rule_id = None
        self._rule_name = None
        self._text = None
        self._type = None

    @property
    def hit_words(self):
        return self._hit_words

    @hit_words.setter
    def hit_words(self, value):
        if isinstance(value, list):
            self._hit_words = list()
            for i in value:
                self._hit_words.append(i)
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def result_tips(self):
        return self._result_tips

    @result_tips.setter
    def result_tips(self, value):
        self._result_tips = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.hit_words:
            if isinstance(self.hit_words, list):
                for i in range(0, len(self.hit_words)):
                    element = self.hit_words[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hit_words[i] = element.to_alipay_dict()
            if hasattr(self.hit_words, 'to_alipay_dict'):
                params['hit_words'] = self.hit_words.to_alipay_dict()
            else:
                params['hit_words'] = self.hit_words
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.result_tips:
            if hasattr(self.result_tips, 'to_alipay_dict'):
                params['result_tips'] = self.result_tips.to_alipay_dict()
            else:
                params['result_tips'] = self.result_tips
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
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
        o = HittedRule()
        if 'hit_words' in d:
            o.hit_words = d['hit_words']
        if 'level' in d:
            o.level = d['level']
        if 'result_tips' in d:
            o.result_tips = d['result_tips']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'text' in d:
            o.text = d['text']
        if 'type' in d:
            o.type = d['type']
        return o


