#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AnswerContent import AnswerContent


class ChatResponse(object):

    def __init__(self):
        self._answer_content = None
        self._biz_type = None
        self._sub_biz_type = None

    @property
    def answer_content(self):
        return self._answer_content

    @answer_content.setter
    def answer_content(self, value):
        if isinstance(value, AnswerContent):
            self._answer_content = value
        else:
            self._answer_content = AnswerContent.from_alipay_dict(value)
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer_content:
            if hasattr(self.answer_content, 'to_alipay_dict'):
                params['answer_content'] = self.answer_content.to_alipay_dict()
            else:
                params['answer_content'] = self.answer_content
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatResponse()
        if 'answer_content' in d:
            o.answer_content = d['answer_content']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


