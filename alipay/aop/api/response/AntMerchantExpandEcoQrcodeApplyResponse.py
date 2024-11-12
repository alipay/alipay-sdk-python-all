#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetEcoQrcodeInfo import AssetEcoQrcodeInfo


class AntMerchantExpandEcoQrcodeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandEcoQrcodeApplyResponse, self).__init__()
        self._qrcode_info = None

    @property
    def qrcode_info(self):
        return self._qrcode_info

    @qrcode_info.setter
    def qrcode_info(self, value):
        if isinstance(value, AssetEcoQrcodeInfo):
            self._qrcode_info = value
        else:
            self._qrcode_info = AssetEcoQrcodeInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandEcoQrcodeApplyResponse, self).parse_response_content(response_content)
        if 'qrcode_info' in response:
            self.qrcode_info = response['qrcode_info']
