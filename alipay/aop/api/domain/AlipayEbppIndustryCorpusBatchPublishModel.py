#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCorpusBatchPublishModel(object):

    def __init__(self):
        self._bot_id = None
        self._corpus_type = None
        self._out_corpus_id_list = None
        self._publish_name = None
        self._publish_type = None

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
    def out_corpus_id_list(self):
        return self._out_corpus_id_list

    @out_corpus_id_list.setter
    def out_corpus_id_list(self, value):
        if isinstance(value, list):
            self._out_corpus_id_list = list()
            for i in value:
                self._out_corpus_id_list.append(i)
    @property
    def publish_name(self):
        return self._publish_name

    @publish_name.setter
    def publish_name(self, value):
        self._publish_name = value
    @property
    def publish_type(self):
        return self._publish_type

    @publish_type.setter
    def publish_type(self, value):
        self._publish_type = value


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
        if self.out_corpus_id_list:
            if isinstance(self.out_corpus_id_list, list):
                for i in range(0, len(self.out_corpus_id_list)):
                    element = self.out_corpus_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_corpus_id_list[i] = element.to_alipay_dict()
            if hasattr(self.out_corpus_id_list, 'to_alipay_dict'):
                params['out_corpus_id_list'] = self.out_corpus_id_list.to_alipay_dict()
            else:
                params['out_corpus_id_list'] = self.out_corpus_id_list
        if self.publish_name:
            if hasattr(self.publish_name, 'to_alipay_dict'):
                params['publish_name'] = self.publish_name.to_alipay_dict()
            else:
                params['publish_name'] = self.publish_name
        if self.publish_type:
            if hasattr(self.publish_type, 'to_alipay_dict'):
                params['publish_type'] = self.publish_type.to_alipay_dict()
            else:
                params['publish_type'] = self.publish_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCorpusBatchPublishModel()
        if 'bot_id' in d:
            o.bot_id = d['bot_id']
        if 'corpus_type' in d:
            o.corpus_type = d['corpus_type']
        if 'out_corpus_id_list' in d:
            o.out_corpus_id_list = d['out_corpus_id_list']
        if 'publish_name' in d:
            o.publish_name = d['publish_name']
        if 'publish_type' in d:
            o.publish_type = d['publish_type']
        return o


