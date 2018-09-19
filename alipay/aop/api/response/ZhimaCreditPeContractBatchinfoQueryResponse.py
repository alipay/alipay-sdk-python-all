#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeContractBatchinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeContractBatchinfoQueryResponse, self).__init__()
        self._batch_record = None
        self._data_content = None
        self._md_5_sign = None
        self._next_batch_index = None
        self._total_record = None
        self._transaction_id = None

    @property
    def batch_record(self):
        return self._batch_record

    @batch_record.setter
    def batch_record(self, value):
        self._batch_record = value
    @property
    def data_content(self):
        return self._data_content

    @data_content.setter
    def data_content(self, value):
        self._data_content = value
    @property
    def md_5_sign(self):
        return self._md_5_sign

    @md_5_sign.setter
    def md_5_sign(self, value):
        self._md_5_sign = value
    @property
    def next_batch_index(self):
        return self._next_batch_index

    @next_batch_index.setter
    def next_batch_index(self, value):
        self._next_batch_index = value
    @property
    def total_record(self):
        return self._total_record

    @total_record.setter
    def total_record(self, value):
        self._total_record = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeContractBatchinfoQueryResponse, self).parse_response_content(response_content)
        if 'batch_record' in response:
            self.batch_record = response['batch_record']
        if 'data_content' in response:
            self.data_content = response['data_content']
        if 'md_5_sign' in response:
            self.md_5_sign = response['md_5_sign']
        if 'next_batch_index' in response:
            self.next_batch_index = response['next_batch_index']
        if 'total_record' in response:
            self.total_record = response['total_record']
        if 'transaction_id' in response:
            self.transaction_id = response['transaction_id']
