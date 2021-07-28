#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FinanceFileInfo import FinanceFileInfo


class AnttechBlockchainFinanceFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceFileUploadResponse, self).__init__()
        self._file_info = None

    @property
    def file_info(self):
        return self._file_info

    @file_info.setter
    def file_info(self, value):
        if isinstance(value, FinanceFileInfo):
            self._file_info = value
        else:
            self._file_info = FinanceFileInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceFileUploadResponse, self).parse_response_content(response_content)
        if 'file_info' in response:
            self.file_info = response['file_info']
