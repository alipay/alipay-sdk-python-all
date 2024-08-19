#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnswerKnowledgeDetail(object):

    def __init__(self):
        self._knowledge_content = None
        self._knowledge_id = None
        self._knowledge_title = None
        self._knowledge_type = None

    @property
    def knowledge_content(self):
        return self._knowledge_content

    @knowledge_content.setter
    def knowledge_content(self, value):
        self._knowledge_content = value
    @property
    def knowledge_id(self):
        return self._knowledge_id

    @knowledge_id.setter
    def knowledge_id(self, value):
        self._knowledge_id = value
    @property
    def knowledge_title(self):
        return self._knowledge_title

    @knowledge_title.setter
    def knowledge_title(self, value):
        self._knowledge_title = value
    @property
    def knowledge_type(self):
        return self._knowledge_type

    @knowledge_type.setter
    def knowledge_type(self, value):
        self._knowledge_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.knowledge_content:
            if hasattr(self.knowledge_content, 'to_alipay_dict'):
                params['knowledge_content'] = self.knowledge_content.to_alipay_dict()
            else:
                params['knowledge_content'] = self.knowledge_content
        if self.knowledge_id:
            if hasattr(self.knowledge_id, 'to_alipay_dict'):
                params['knowledge_id'] = self.knowledge_id.to_alipay_dict()
            else:
                params['knowledge_id'] = self.knowledge_id
        if self.knowledge_title:
            if hasattr(self.knowledge_title, 'to_alipay_dict'):
                params['knowledge_title'] = self.knowledge_title.to_alipay_dict()
            else:
                params['knowledge_title'] = self.knowledge_title
        if self.knowledge_type:
            if hasattr(self.knowledge_type, 'to_alipay_dict'):
                params['knowledge_type'] = self.knowledge_type.to_alipay_dict()
            else:
                params['knowledge_type'] = self.knowledge_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnswerKnowledgeDetail()
        if 'knowledge_content' in d:
            o.knowledge_content = d['knowledge_content']
        if 'knowledge_id' in d:
            o.knowledge_id = d['knowledge_id']
        if 'knowledge_title' in d:
            o.knowledge_title = d['knowledge_title']
        if 'knowledge_type' in d:
            o.knowledge_type = d['knowledge_type']
        return o


