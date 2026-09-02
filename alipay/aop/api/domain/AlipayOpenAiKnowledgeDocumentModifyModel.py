#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAiKnowledgeDocumentModifyModel(object):

    def __init__(self):
        self._document_id = None
        self._file_id = None
        self._knowledge_base_id = None
        self._update_mode = None

    @property
    def document_id(self):
        return self._document_id

    @document_id.setter
    def document_id(self, value):
        self._document_id = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def knowledge_base_id(self):
        return self._knowledge_base_id

    @knowledge_base_id.setter
    def knowledge_base_id(self, value):
        self._knowledge_base_id = value
    @property
    def update_mode(self):
        return self._update_mode

    @update_mode.setter
    def update_mode(self, value):
        self._update_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.document_id:
            if hasattr(self.document_id, 'to_alipay_dict'):
                params['document_id'] = self.document_id.to_alipay_dict()
            else:
                params['document_id'] = self.document_id
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.knowledge_base_id:
            if hasattr(self.knowledge_base_id, 'to_alipay_dict'):
                params['knowledge_base_id'] = self.knowledge_base_id.to_alipay_dict()
            else:
                params['knowledge_base_id'] = self.knowledge_base_id
        if self.update_mode:
            if hasattr(self.update_mode, 'to_alipay_dict'):
                params['update_mode'] = self.update_mode.to_alipay_dict()
            else:
                params['update_mode'] = self.update_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAiKnowledgeDocumentModifyModel()
        if 'document_id' in d:
            o.document_id = d['document_id']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'knowledge_base_id' in d:
            o.knowledge_base_id = d['knowledge_base_id']
        if 'update_mode' in d:
            o.update_mode = d['update_mode']
        return o


