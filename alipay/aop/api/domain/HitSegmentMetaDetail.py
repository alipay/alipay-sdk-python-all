#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HitSegmentMetaDetail(object):

    def __init__(self):
        self._document_id = None
        self._document_name = None
        self._knowledge_base_id = None
        self._segment_id = None
        self._segment_position = None

    @property
    def document_id(self):
        return self._document_id

    @document_id.setter
    def document_id(self, value):
        self._document_id = value
    @property
    def document_name(self):
        return self._document_name

    @document_name.setter
    def document_name(self, value):
        self._document_name = value
    @property
    def knowledge_base_id(self):
        return self._knowledge_base_id

    @knowledge_base_id.setter
    def knowledge_base_id(self, value):
        self._knowledge_base_id = value
    @property
    def segment_id(self):
        return self._segment_id

    @segment_id.setter
    def segment_id(self, value):
        self._segment_id = value
    @property
    def segment_position(self):
        return self._segment_position

    @segment_position.setter
    def segment_position(self, value):
        self._segment_position = value


    def to_alipay_dict(self):
        params = dict()
        if self.document_id:
            if hasattr(self.document_id, 'to_alipay_dict'):
                params['document_id'] = self.document_id.to_alipay_dict()
            else:
                params['document_id'] = self.document_id
        if self.document_name:
            if hasattr(self.document_name, 'to_alipay_dict'):
                params['document_name'] = self.document_name.to_alipay_dict()
            else:
                params['document_name'] = self.document_name
        if self.knowledge_base_id:
            if hasattr(self.knowledge_base_id, 'to_alipay_dict'):
                params['knowledge_base_id'] = self.knowledge_base_id.to_alipay_dict()
            else:
                params['knowledge_base_id'] = self.knowledge_base_id
        if self.segment_id:
            if hasattr(self.segment_id, 'to_alipay_dict'):
                params['segment_id'] = self.segment_id.to_alipay_dict()
            else:
                params['segment_id'] = self.segment_id
        if self.segment_position:
            if hasattr(self.segment_position, 'to_alipay_dict'):
                params['segment_position'] = self.segment_position.to_alipay_dict()
            else:
                params['segment_position'] = self.segment_position
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HitSegmentMetaDetail()
        if 'document_id' in d:
            o.document_id = d['document_id']
        if 'document_name' in d:
            o.document_name = d['document_name']
        if 'knowledge_base_id' in d:
            o.knowledge_base_id = d['knowledge_base_id']
        if 'segment_id' in d:
            o.segment_id = d['segment_id']
        if 'segment_position' in d:
            o.segment_position = d['segment_position']
        return o


