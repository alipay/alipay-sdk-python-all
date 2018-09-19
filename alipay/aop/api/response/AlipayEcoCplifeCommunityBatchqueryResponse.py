#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CPCommunitySet import CPCommunitySet


class AlipayEcoCplifeCommunityBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeCommunityBatchqueryResponse, self).__init__()
        self._community_list = None
        self._current_page_num = None
        self._total_community_count = None

    @property
    def community_list(self):
        return self._community_list

    @community_list.setter
    def community_list(self, value):
        if isinstance(value, list):
            self._community_list = list()
            for i in value:
                if isinstance(i, CPCommunitySet):
                    self._community_list.append(i)
                else:
                    self._community_list.append(CPCommunitySet.from_alipay_dict(i))
    @property
    def current_page_num(self):
        return self._current_page_num

    @current_page_num.setter
    def current_page_num(self, value):
        self._current_page_num = value
    @property
    def total_community_count(self):
        return self._total_community_count

    @total_community_count.setter
    def total_community_count(self, value):
        self._total_community_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeCommunityBatchqueryResponse, self).parse_response_content(response_content)
        if 'community_list' in response:
            self.community_list = response['community_list']
        if 'current_page_num' in response:
            self.current_page_num = response['current_page_num']
        if 'total_community_count' in response:
            self.total_community_count = response['total_community_count']
