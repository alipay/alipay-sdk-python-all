#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalLlmAnswerDTO(object):

    def __init__(self):
        self._content = None
        self._query = None
        self._seq_num = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def seq_num(self):
        return self._seq_num

    @seq_num.setter
    def seq_num(self, value):
        self._seq_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.seq_num:
            if hasattr(self.seq_num, 'to_alipay_dict'):
                params['seq_num'] = self.seq_num.to_alipay_dict()
            else:
                params['seq_num'] = self.seq_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalLlmAnswerDTO()
        if 'content' in d:
            o.content = d['content']
        if 'query' in d:
            o.query = d['query']
        if 'seq_num' in d:
            o.seq_num = d['seq_num']
        return o


