#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CorpusPublishTaskResult import CorpusPublishTaskResult
from alipay.aop.api.domain.CorpusSyncResult import CorpusSyncResult


class AlipayEbppIndustryCorpusCommonQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCorpusCommonQueryResponse, self).__init__()
        self._corpus_publish_task_result_list = None
        self._corpus_sync_result = None

    @property
    def corpus_publish_task_result_list(self):
        return self._corpus_publish_task_result_list

    @corpus_publish_task_result_list.setter
    def corpus_publish_task_result_list(self, value):
        if isinstance(value, CorpusPublishTaskResult):
            self._corpus_publish_task_result_list = value
        else:
            self._corpus_publish_task_result_list = CorpusPublishTaskResult.from_alipay_dict(value)
    @property
    def corpus_sync_result(self):
        return self._corpus_sync_result

    @corpus_sync_result.setter
    def corpus_sync_result(self, value):
        if isinstance(value, CorpusSyncResult):
            self._corpus_sync_result = value
        else:
            self._corpus_sync_result = CorpusSyncResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCorpusCommonQueryResponse, self).parse_response_content(response_content)
        if 'corpus_publish_task_result_list' in response:
            self.corpus_publish_task_result_list = response['corpus_publish_task_result_list']
        if 'corpus_sync_result' in response:
            self.corpus_sync_result = response['corpus_sync_result']
