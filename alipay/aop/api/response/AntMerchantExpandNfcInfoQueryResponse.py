#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetQrcodeInfoDTO import AssetQrcodeInfoDTO


class AntMerchantExpandNfcInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandNfcInfoQueryResponse, self).__init__()
        self._nfc_info_list = None

    @property
    def nfc_info_list(self):
        return self._nfc_info_list

    @nfc_info_list.setter
    def nfc_info_list(self, value):
        if isinstance(value, list):
            self._nfc_info_list = list()
            for i in value:
                if isinstance(i, AssetQrcodeInfoDTO):
                    self._nfc_info_list.append(i)
                else:
                    self._nfc_info_list.append(AssetQrcodeInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandNfcInfoQueryResponse, self).parse_response_content(response_content)
        if 'nfc_info_list' in response:
            self.nfc_info_list = response['nfc_info_list']
