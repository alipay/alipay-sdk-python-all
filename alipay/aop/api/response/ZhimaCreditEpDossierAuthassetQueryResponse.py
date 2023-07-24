#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpAssetInfo import EpAssetInfo


class ZhimaCreditEpDossierAuthassetQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierAuthassetQueryResponse, self).__init__()
        self._asset_infos = None
        self._has_authed = None

    @property
    def asset_infos(self):
        return self._asset_infos

    @asset_infos.setter
    def asset_infos(self, value):
        if isinstance(value, list):
            self._asset_infos = list()
            for i in value:
                if isinstance(i, EpAssetInfo):
                    self._asset_infos.append(i)
                else:
                    self._asset_infos.append(EpAssetInfo.from_alipay_dict(i))
    @property
    def has_authed(self):
        return self._has_authed

    @has_authed.setter
    def has_authed(self, value):
        self._has_authed = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierAuthassetQueryResponse, self).parse_response_content(response_content)
        if 'asset_infos' in response:
            self.asset_infos = response['asset_infos']
        if 'has_authed' in response:
            self.has_authed = response['has_authed']
