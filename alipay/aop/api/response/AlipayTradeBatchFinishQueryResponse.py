#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BatchFinishInfo import BatchFinishInfo


class AlipayTradeBatchFinishQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeBatchFinishQueryResponse, self).__init__()
        self._batch_list = None

    @property
    def batch_list(self):
        return self._batch_list

    @batch_list.setter
    def batch_list(self, value):
        if isinstance(value, list):
            self._batch_list = list()
            for i in value:
                if isinstance(i, BatchFinishInfo):
                    self._batch_list.append(i)
                else:
                    self._batch_list.append(BatchFinishInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeBatchFinishQueryResponse, self).parse_response_content(response_content)
        if 'batch_list' in response:
            self.batch_list = response['batch_list']
