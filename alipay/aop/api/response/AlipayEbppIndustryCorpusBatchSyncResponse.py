#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InterceptedCorpusResult import InterceptedCorpusResult


class AlipayEbppIndustryCorpusBatchSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCorpusBatchSyncResponse, self).__init__()
        self._intercepted_corpus_list = None
        self._sync_batch_id = None
        self._sync_result = None

    @property
    def intercepted_corpus_list(self):
        return self._intercepted_corpus_list

    @intercepted_corpus_list.setter
    def intercepted_corpus_list(self, value):
        if isinstance(value, list):
            self._intercepted_corpus_list = list()
            for i in value:
                if isinstance(i, InterceptedCorpusResult):
                    self._intercepted_corpus_list.append(i)
                else:
                    self._intercepted_corpus_list.append(InterceptedCorpusResult.from_alipay_dict(i))
    @property
    def sync_batch_id(self):
        return self._sync_batch_id

    @sync_batch_id.setter
    def sync_batch_id(self, value):
        self._sync_batch_id = value
    @property
    def sync_result(self):
        return self._sync_result

    @sync_result.setter
    def sync_result(self, value):
        self._sync_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCorpusBatchSyncResponse, self).parse_response_content(response_content)
        if 'intercepted_corpus_list' in response:
            self.intercepted_corpus_list = response['intercepted_corpus_list']
        if 'sync_batch_id' in response:
            self.sync_batch_id = response['sync_batch_id']
        if 'sync_result' in response:
            self.sync_result = response['sync_result']
