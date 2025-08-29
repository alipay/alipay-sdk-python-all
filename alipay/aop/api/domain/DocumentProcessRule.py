#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChunkConfig import ChunkConfig


class DocumentProcessRule(object):

    def __init__(self):
        self._chunk_config = None
        self._chunk_digest = None
        self._similar_question = None

    @property
    def chunk_config(self):
        return self._chunk_config

    @chunk_config.setter
    def chunk_config(self, value):
        if isinstance(value, ChunkConfig):
            self._chunk_config = value
        else:
            self._chunk_config = ChunkConfig.from_alipay_dict(value)
    @property
    def chunk_digest(self):
        return self._chunk_digest

    @chunk_digest.setter
    def chunk_digest(self, value):
        self._chunk_digest = value
    @property
    def similar_question(self):
        return self._similar_question

    @similar_question.setter
    def similar_question(self, value):
        self._similar_question = value


    def to_alipay_dict(self):
        params = dict()
        if self.chunk_config:
            if hasattr(self.chunk_config, 'to_alipay_dict'):
                params['chunk_config'] = self.chunk_config.to_alipay_dict()
            else:
                params['chunk_config'] = self.chunk_config
        if self.chunk_digest:
            if hasattr(self.chunk_digest, 'to_alipay_dict'):
                params['chunk_digest'] = self.chunk_digest.to_alipay_dict()
            else:
                params['chunk_digest'] = self.chunk_digest
        if self.similar_question:
            if hasattr(self.similar_question, 'to_alipay_dict'):
                params['similar_question'] = self.similar_question.to_alipay_dict()
            else:
                params['similar_question'] = self.similar_question
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DocumentProcessRule()
        if 'chunk_config' in d:
            o.chunk_config = d['chunk_config']
        if 'chunk_digest' in d:
            o.chunk_digest = d['chunk_digest']
        if 'similar_question' in d:
            o.similar_question = d['similar_question']
        return o


