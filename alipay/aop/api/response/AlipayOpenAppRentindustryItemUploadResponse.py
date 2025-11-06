#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantSkuUploadResult import MerchantSkuUploadResult


class AlipayOpenAppRentindustryItemUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppRentindustryItemUploadResponse, self).__init__()
        self._upload_result = None

    @property
    def upload_result(self):
        return self._upload_result

    @upload_result.setter
    def upload_result(self, value):
        if isinstance(value, list):
            self._upload_result = list()
            for i in value:
                if isinstance(i, MerchantSkuUploadResult):
                    self._upload_result.append(i)
                else:
                    self._upload_result.append(MerchantSkuUploadResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppRentindustryItemUploadResponse, self).parse_response_content(response_content)
        if 'upload_result' in response:
            self.upload_result = response['upload_result']
