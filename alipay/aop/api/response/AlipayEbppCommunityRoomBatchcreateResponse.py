#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RoomBatchCreateResult import RoomBatchCreateResult


class AlipayEbppCommunityRoomBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityRoomBatchcreateResponse, self).__init__()
        self._fail_count = None
        self._results = None
        self._success_count = None
        self._total_count = None

    @property
    def fail_count(self):
        return self._fail_count

    @fail_count.setter
    def fail_count(self, value):
        self._fail_count = value
    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        if isinstance(value, list):
            self._results = list()
            for i in value:
                if isinstance(i, RoomBatchCreateResult):
                    self._results.append(i)
                else:
                    self._results.append(RoomBatchCreateResult.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityRoomBatchcreateResponse, self).parse_response_content(response_content)
        if 'fail_count' in response:
            self.fail_count = response['fail_count']
        if 'results' in response:
            self.results = response['results']
        if 'success_count' in response:
            self.success_count = response['success_count']
        if 'total_count' in response:
            self.total_count = response['total_count']
