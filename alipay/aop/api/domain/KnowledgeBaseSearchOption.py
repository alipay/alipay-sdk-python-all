#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LegacyPreFilterDetail import LegacyPreFilterDetail


class KnowledgeBaseSearchOption(object):

    def __init__(self):
        self._knowledge_base_id = None
        self._legacy_pre_filters = None

    @property
    def knowledge_base_id(self):
        return self._knowledge_base_id

    @knowledge_base_id.setter
    def knowledge_base_id(self, value):
        self._knowledge_base_id = value
    @property
    def legacy_pre_filters(self):
        return self._legacy_pre_filters

    @legacy_pre_filters.setter
    def legacy_pre_filters(self, value):
        if isinstance(value, list):
            self._legacy_pre_filters = list()
            for i in value:
                if isinstance(i, LegacyPreFilterDetail):
                    self._legacy_pre_filters.append(i)
                else:
                    self._legacy_pre_filters.append(LegacyPreFilterDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.knowledge_base_id:
            if hasattr(self.knowledge_base_id, 'to_alipay_dict'):
                params['knowledge_base_id'] = self.knowledge_base_id.to_alipay_dict()
            else:
                params['knowledge_base_id'] = self.knowledge_base_id
        if self.legacy_pre_filters:
            if isinstance(self.legacy_pre_filters, list):
                for i in range(0, len(self.legacy_pre_filters)):
                    element = self.legacy_pre_filters[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.legacy_pre_filters[i] = element.to_alipay_dict()
            if hasattr(self.legacy_pre_filters, 'to_alipay_dict'):
                params['legacy_pre_filters'] = self.legacy_pre_filters.to_alipay_dict()
            else:
                params['legacy_pre_filters'] = self.legacy_pre_filters
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KnowledgeBaseSearchOption()
        if 'knowledge_base_id' in d:
            o.knowledge_base_id = d['knowledge_base_id']
        if 'legacy_pre_filters' in d:
            o.legacy_pre_filters = d['legacy_pre_filters']
        return o


