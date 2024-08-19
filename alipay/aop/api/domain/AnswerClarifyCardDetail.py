#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnswerClarifyCardDetail(object):

    def __init__(self):
        self._dst_list = None
        self._follow_question = None

    @property
    def dst_list(self):
        return self._dst_list

    @dst_list.setter
    def dst_list(self, value):
        if isinstance(value, list):
            self._dst_list = list()
            for i in value:
                self._dst_list.append(i)
    @property
    def follow_question(self):
        return self._follow_question

    @follow_question.setter
    def follow_question(self, value):
        self._follow_question = value


    def to_alipay_dict(self):
        params = dict()
        if self.dst_list:
            if isinstance(self.dst_list, list):
                for i in range(0, len(self.dst_list)):
                    element = self.dst_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dst_list[i] = element.to_alipay_dict()
            if hasattr(self.dst_list, 'to_alipay_dict'):
                params['dst_list'] = self.dst_list.to_alipay_dict()
            else:
                params['dst_list'] = self.dst_list
        if self.follow_question:
            if hasattr(self.follow_question, 'to_alipay_dict'):
                params['follow_question'] = self.follow_question.to_alipay_dict()
            else:
                params['follow_question'] = self.follow_question
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnswerClarifyCardDetail()
        if 'dst_list' in d:
            o.dst_list = d['dst_list']
        if 'follow_question' in d:
            o.follow_question = d['follow_question']
        return o


