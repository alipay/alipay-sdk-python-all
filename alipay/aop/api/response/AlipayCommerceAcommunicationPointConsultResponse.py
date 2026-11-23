#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TopUpPointAssetInfo import TopUpPointAssetInfo


class AlipayCommerceAcommunicationPointConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationPointConsultResponse, self).__init__()
        self._asset_consult_infos = None

    @property
    def asset_consult_infos(self):
        return self._asset_consult_infos

    @asset_consult_infos.setter
    def asset_consult_infos(self, value):
        if isinstance(value, list):
            self._asset_consult_infos = list()
            for i in value:
                if isinstance(i, TopUpPointAssetInfo):
                    self._asset_consult_infos.append(i)
                else:
                    self._asset_consult_infos.append(TopUpPointAssetInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationPointConsultResponse, self).parse_response_content(response_content)
        if 'asset_consult_infos' in response:
            self.asset_consult_infos = response['asset_consult_infos']
