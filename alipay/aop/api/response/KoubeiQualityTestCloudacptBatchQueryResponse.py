#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenBatch import OpenBatch


class KoubeiQualityTestCloudacptBatchQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiQualityTestCloudacptBatchQueryResponse, self).__init__()
        self._activity_id = None
        self._batch_list = None
        self._batch_num = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def batch_list(self):
        return self._batch_list

    @batch_list.setter
    def batch_list(self, value):
        if isinstance(value, list):
            self._batch_list = list()
            for i in value:
                if isinstance(i, OpenBatch):
                    self._batch_list.append(i)
                else:
                    self._batch_list.append(OpenBatch.from_alipay_dict(i))
    @property
    def batch_num(self):
        return self._batch_num

    @batch_num.setter
    def batch_num(self, value):
        self._batch_num = value

    def parse_response_content(self, response_content):
        response = super(KoubeiQualityTestCloudacptBatchQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'batch_list' in response:
            self.batch_list = response['batch_list']
        if 'batch_num' in response:
            self.batch_num = response['batch_num']
