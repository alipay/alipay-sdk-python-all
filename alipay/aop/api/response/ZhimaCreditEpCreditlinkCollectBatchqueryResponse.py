#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCreditlinkCollectBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCreditlinkCollectBatchqueryResponse, self).__init__()
        self._contents = None
        self._cur_page_number = None
        self._data_status = None
        self._data_type = None
        self._merchant_request_id = None
        self._total_count = None
        self._total_page_number = None

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        self._contents = value
    @property
    def cur_page_number(self):
        return self._cur_page_number

    @cur_page_number.setter
    def cur_page_number(self, value):
        self._cur_page_number = value
    @property
    def data_status(self):
        return self._data_status

    @data_status.setter
    def data_status(self, value):
        self._data_status = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page_number(self):
        return self._total_page_number

    @total_page_number.setter
    def total_page_number(self, value):
        self._total_page_number = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCreditlinkCollectBatchqueryResponse, self).parse_response_content(response_content)
        if 'contents' in response:
            self.contents = response['contents']
        if 'cur_page_number' in response:
            self.cur_page_number = response['cur_page_number']
        if 'data_status' in response:
            self.data_status = response['data_status']
        if 'data_type' in response:
            self.data_type = response['data_type']
        if 'merchant_request_id' in response:
            self.merchant_request_id = response['merchant_request_id']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page_number' in response:
            self.total_page_number = response['total_page_number']
