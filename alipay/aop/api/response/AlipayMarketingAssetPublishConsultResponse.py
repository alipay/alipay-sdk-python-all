#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenAssetPublishConsultResult import OpenAssetPublishConsultResult


class AlipayMarketingAssetPublishConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingAssetPublishConsultResponse, self).__init__()
        self._open_asset_publish_consult_results = None

    @property
    def open_asset_publish_consult_results(self):
        return self._open_asset_publish_consult_results

    @open_asset_publish_consult_results.setter
    def open_asset_publish_consult_results(self, value):
        if isinstance(value, list):
            self._open_asset_publish_consult_results = list()
            for i in value:
                if isinstance(i, OpenAssetPublishConsultResult):
                    self._open_asset_publish_consult_results.append(i)
                else:
                    self._open_asset_publish_consult_results.append(OpenAssetPublishConsultResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingAssetPublishConsultResponse, self).parse_response_content(response_content)
        if 'open_asset_publish_consult_results' in response:
            self.open_asset_publish_consult_results = response['open_asset_publish_consult_results']
