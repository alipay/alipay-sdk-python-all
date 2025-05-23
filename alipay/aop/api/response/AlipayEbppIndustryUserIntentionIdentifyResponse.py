#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IntentionInfo import IntentionInfo


class AlipayEbppIndustryUserIntentionIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryUserIntentionIdentifyResponse, self).__init__()
        self._intention_info_list = None
        self._query_extension_list = None
        self._query_rewrite = None

    @property
    def intention_info_list(self):
        return self._intention_info_list

    @intention_info_list.setter
    def intention_info_list(self, value):
        if isinstance(value, IntentionInfo):
            self._intention_info_list = value
        else:
            self._intention_info_list = IntentionInfo.from_alipay_dict(value)
    @property
    def query_extension_list(self):
        return self._query_extension_list

    @query_extension_list.setter
    def query_extension_list(self, value):
        if isinstance(value, list):
            self._query_extension_list = list()
            for i in value:
                self._query_extension_list.append(i)
    @property
    def query_rewrite(self):
        return self._query_rewrite

    @query_rewrite.setter
    def query_rewrite(self, value):
        self._query_rewrite = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryUserIntentionIdentifyResponse, self).parse_response_content(response_content)
        if 'intention_info_list' in response:
            self.intention_info_list = response['intention_info_list']
        if 'query_extension_list' in response:
            self.query_extension_list = response['query_extension_list']
        if 'query_rewrite' in response:
            self.query_rewrite = response['query_rewrite']
