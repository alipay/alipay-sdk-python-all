#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDapplyOrderBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyOrderBatchcreateResponse, self).__init__()
        self._batch_no = None
        self._excel_validate_detail_file = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def excel_validate_detail_file(self):
        return self._excel_validate_detail_file

    @excel_validate_detail_file.setter
    def excel_validate_detail_file(self, value):
        self._excel_validate_detail_file = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyOrderBatchcreateResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'excel_validate_detail_file' in response:
            self.excel_validate_detail_file = response['excel_validate_detail_file']
