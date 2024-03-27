#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RelatedDocumentFragments import RelatedDocumentFragments


class DocumentKnowledgeDetail(object):

    def __init__(self):
        self._document_answer = None
        self._related_document_fragments = None
        self._stream_output = None

    @property
    def document_answer(self):
        return self._document_answer

    @document_answer.setter
    def document_answer(self, value):
        self._document_answer = value
    @property
    def related_document_fragments(self):
        return self._related_document_fragments

    @related_document_fragments.setter
    def related_document_fragments(self, value):
        if isinstance(value, list):
            self._related_document_fragments = list()
            for i in value:
                if isinstance(i, RelatedDocumentFragments):
                    self._related_document_fragments.append(i)
                else:
                    self._related_document_fragments.append(RelatedDocumentFragments.from_alipay_dict(i))
    @property
    def stream_output(self):
        return self._stream_output

    @stream_output.setter
    def stream_output(self, value):
        self._stream_output = value


    def to_alipay_dict(self):
        params = dict()
        if self.document_answer:
            if hasattr(self.document_answer, 'to_alipay_dict'):
                params['document_answer'] = self.document_answer.to_alipay_dict()
            else:
                params['document_answer'] = self.document_answer
        if self.related_document_fragments:
            if isinstance(self.related_document_fragments, list):
                for i in range(0, len(self.related_document_fragments)):
                    element = self.related_document_fragments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_document_fragments[i] = element.to_alipay_dict()
            if hasattr(self.related_document_fragments, 'to_alipay_dict'):
                params['related_document_fragments'] = self.related_document_fragments.to_alipay_dict()
            else:
                params['related_document_fragments'] = self.related_document_fragments
        if self.stream_output:
            if hasattr(self.stream_output, 'to_alipay_dict'):
                params['stream_output'] = self.stream_output.to_alipay_dict()
            else:
                params['stream_output'] = self.stream_output
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DocumentKnowledgeDetail()
        if 'document_answer' in d:
            o.document_answer = d['document_answer']
        if 'related_document_fragments' in d:
            o.related_document_fragments = d['related_document_fragments']
        if 'stream_output' in d:
            o.stream_output = d['stream_output']
        return o


