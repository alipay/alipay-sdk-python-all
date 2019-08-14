#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandExpressChangeSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandExpressChangeSyncResponse, self).__init__()
        self._upload_result = None

    @property
    def upload_result(self):
        return self._upload_result

    @upload_result.setter
    def upload_result(self, value):
        if isinstance(value, AssetResult):
            self._upload_result = value
        else:
            self._upload_result = AssetResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandExpressChangeSyncResponse, self).parse_response_content(response_content)
        if 'upload_result' in response:
            self.upload_result = response['upload_result']
