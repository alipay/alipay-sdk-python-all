#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContentErrorInfo import ContentErrorInfo


class AntMerchantExpandQualityAssetproduceDetectResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandQualityAssetproduceDetectResponse, self).__init__()
        self._detect_error_code = None
        self._detect_error_desc = None
        self._detect_error_info = None
        self._detect_success = None

    @property
    def detect_error_code(self):
        return self._detect_error_code

    @detect_error_code.setter
    def detect_error_code(self, value):
        self._detect_error_code = value
    @property
    def detect_error_desc(self):
        return self._detect_error_desc

    @detect_error_desc.setter
    def detect_error_desc(self, value):
        self._detect_error_desc = value
    @property
    def detect_error_info(self):
        return self._detect_error_info

    @detect_error_info.setter
    def detect_error_info(self, value):
        if isinstance(value, ContentErrorInfo):
            self._detect_error_info = value
        else:
            self._detect_error_info = ContentErrorInfo.from_alipay_dict(value)
    @property
    def detect_success(self):
        return self._detect_success

    @detect_success.setter
    def detect_success(self, value):
        self._detect_success = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandQualityAssetproduceDetectResponse, self).parse_response_content(response_content)
        if 'detect_error_code' in response:
            self.detect_error_code = response['detect_error_code']
        if 'detect_error_desc' in response:
            self.detect_error_desc = response['detect_error_desc']
        if 'detect_error_info' in response:
            self.detect_error_info = response['detect_error_info']
        if 'detect_success' in response:
            self.detect_success = response['detect_success']
