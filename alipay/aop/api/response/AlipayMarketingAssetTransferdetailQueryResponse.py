#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetTransferDetailDTO import AssetTransferDetailDTO


class AlipayMarketingAssetTransferdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingAssetTransferdetailQueryResponse, self).__init__()
        self._details = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, AssetTransferDetailDTO):
                    self._details.append(i)
                else:
                    self._details.append(AssetTransferDetailDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingAssetTransferdetailQueryResponse, self).parse_response_content(response_content)
        if 'details' in response:
            self.details = response['details']
