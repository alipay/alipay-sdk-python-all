#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DocumentKnowledgeDetail import DocumentKnowledgeDetail
from alipay.aop.api.domain.DstDetail import DstDetail
from alipay.aop.api.domain.KnowledgeDetail import KnowledgeDetail
from alipay.aop.api.domain.RecommendDetail import RecommendDetail
from alipay.aop.api.domain.TextDetail import TextDetail


class RobotAnswer(object):

    def __init__(self):
        self._document_knowledge = None
        self._dst = None
        self._knowledge = None
        self._recommends = None
        self._text = None

    @property
    def document_knowledge(self):
        return self._document_knowledge

    @document_knowledge.setter
    def document_knowledge(self, value):
        if isinstance(value, DocumentKnowledgeDetail):
            self._document_knowledge = value
        else:
            self._document_knowledge = DocumentKnowledgeDetail.from_alipay_dict(value)
    @property
    def dst(self):
        return self._dst

    @dst.setter
    def dst(self, value):
        if isinstance(value, DstDetail):
            self._dst = value
        else:
            self._dst = DstDetail.from_alipay_dict(value)
    @property
    def knowledge(self):
        return self._knowledge

    @knowledge.setter
    def knowledge(self, value):
        if isinstance(value, KnowledgeDetail):
            self._knowledge = value
        else:
            self._knowledge = KnowledgeDetail.from_alipay_dict(value)
    @property
    def recommends(self):
        return self._recommends

    @recommends.setter
    def recommends(self, value):
        if isinstance(value, list):
            self._recommends = list()
            for i in value:
                if isinstance(i, RecommendDetail):
                    self._recommends.append(i)
                else:
                    self._recommends.append(RecommendDetail.from_alipay_dict(i))
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, TextDetail):
            self._text = value
        else:
            self._text = TextDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.document_knowledge:
            if hasattr(self.document_knowledge, 'to_alipay_dict'):
                params['document_knowledge'] = self.document_knowledge.to_alipay_dict()
            else:
                params['document_knowledge'] = self.document_knowledge
        if self.dst:
            if hasattr(self.dst, 'to_alipay_dict'):
                params['dst'] = self.dst.to_alipay_dict()
            else:
                params['dst'] = self.dst
        if self.knowledge:
            if hasattr(self.knowledge, 'to_alipay_dict'):
                params['knowledge'] = self.knowledge.to_alipay_dict()
            else:
                params['knowledge'] = self.knowledge
        if self.recommends:
            if isinstance(self.recommends, list):
                for i in range(0, len(self.recommends)):
                    element = self.recommends[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.recommends[i] = element.to_alipay_dict()
            if hasattr(self.recommends, 'to_alipay_dict'):
                params['recommends'] = self.recommends.to_alipay_dict()
            else:
                params['recommends'] = self.recommends
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
        o = RobotAnswer()
        if 'document_knowledge' in d:
            o.document_knowledge = d['document_knowledge']
        if 'dst' in d:
            o.dst = d['dst']
        if 'knowledge' in d:
            o.knowledge = d['knowledge']
        if 'recommends' in d:
            o.recommends = d['recommends']
        if 'text' in d:
            o.text = d['text']
        return o


