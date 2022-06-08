#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetSubFeedbackInfo import AssetSubFeedbackInfo


class AntMerchantExpandAssetinfoCheckSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetinfoCheckSyncResponse, self).__init__()
        self._batch_no = None
        self._error_code = None
        self._error_desc = None
        self._sub_check_infos = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def sub_check_infos(self):
        return self._sub_check_infos

    @sub_check_infos.setter
    def sub_check_infos(self, value):
        if isinstance(value, list):
            self._sub_check_infos = list()
            for i in value:
                if isinstance(i, AssetSubFeedbackInfo):
                    self._sub_check_infos.append(i)
                else:
                    self._sub_check_infos.append(AssetSubFeedbackInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetinfoCheckSyncResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_desc' in response:
            self.error_desc = response['error_desc']
        if 'sub_check_infos' in response:
            self.sub_check_infos = response['sub_check_infos']
