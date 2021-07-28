#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIotdeviceOnlinedataUploadResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIotdeviceOnlinedataUploadResponse, self).__init__()
        self._onlinedata_upload_result = None

    @property
    def onlinedata_upload_result(self):
        return self._onlinedata_upload_result

    @onlinedata_upload_result.setter
    def onlinedata_upload_result(self, value):
        self._onlinedata_upload_result = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIotdeviceOnlinedataUploadResponse, self).parse_response_content(response_content)
        if 'onlinedata_upload_result' in response:
            self.onlinedata_upload_result = response['onlinedata_upload_result']
