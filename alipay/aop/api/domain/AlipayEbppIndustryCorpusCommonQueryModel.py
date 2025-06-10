#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CorpusPublishTaskQueryParam import CorpusPublishTaskQueryParam


class AlipayEbppIndustryCorpusCommonQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._corpus_publish_task_query_param = None
        self._corpus_sync_batch_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def corpus_publish_task_query_param(self):
        return self._corpus_publish_task_query_param

    @corpus_publish_task_query_param.setter
    def corpus_publish_task_query_param(self, value):
        if isinstance(value, CorpusPublishTaskQueryParam):
            self._corpus_publish_task_query_param = value
        else:
            self._corpus_publish_task_query_param = CorpusPublishTaskQueryParam.from_alipay_dict(value)
    @property
    def corpus_sync_batch_id(self):
        return self._corpus_sync_batch_id

    @corpus_sync_batch_id.setter
    def corpus_sync_batch_id(self, value):
        self._corpus_sync_batch_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.corpus_publish_task_query_param:
            if hasattr(self.corpus_publish_task_query_param, 'to_alipay_dict'):
                params['corpus_publish_task_query_param'] = self.corpus_publish_task_query_param.to_alipay_dict()
            else:
                params['corpus_publish_task_query_param'] = self.corpus_publish_task_query_param
        if self.corpus_sync_batch_id:
            if hasattr(self.corpus_sync_batch_id, 'to_alipay_dict'):
                params['corpus_sync_batch_id'] = self.corpus_sync_batch_id.to_alipay_dict()
            else:
                params['corpus_sync_batch_id'] = self.corpus_sync_batch_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCorpusCommonQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'corpus_publish_task_query_param' in d:
            o.corpus_publish_task_query_param = d['corpus_publish_task_query_param']
        if 'corpus_sync_batch_id' in d:
            o.corpus_sync_batch_id = d['corpus_sync_batch_id']
        return o


