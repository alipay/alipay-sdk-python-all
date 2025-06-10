#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCorpusDetailQueryModel(object):

    def __init__(self):
        self._bot_id = None
        self._corpus_type = None
        self._out_corpus_id = None

    @property
    def bot_id(self):
        return self._bot_id

    @bot_id.setter
    def bot_id(self, value):
        self._bot_id = value
    @property
    def corpus_type(self):
        return self._corpus_type

    @corpus_type.setter
    def corpus_type(self, value):
        self._corpus_type = value
    @property
    def out_corpus_id(self):
        return self._out_corpus_id

    @out_corpus_id.setter
    def out_corpus_id(self, value):
        self._out_corpus_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bot_id:
            if hasattr(self.bot_id, 'to_alipay_dict'):
                params['bot_id'] = self.bot_id.to_alipay_dict()
            else:
                params['bot_id'] = self.bot_id
        if self.corpus_type:
            if hasattr(self.corpus_type, 'to_alipay_dict'):
                params['corpus_type'] = self.corpus_type.to_alipay_dict()
            else:
                params['corpus_type'] = self.corpus_type
        if self.out_corpus_id:
            if hasattr(self.out_corpus_id, 'to_alipay_dict'):
                params['out_corpus_id'] = self.out_corpus_id.to_alipay_dict()
            else:
                params['out_corpus_id'] = self.out_corpus_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCorpusDetailQueryModel()
        if 'bot_id' in d:
            o.bot_id = d['bot_id']
        if 'corpus_type' in d:
            o.corpus_type = d['corpus_type']
        if 'out_corpus_id' in d:
            o.out_corpus_id = d['out_corpus_id']
        return o


