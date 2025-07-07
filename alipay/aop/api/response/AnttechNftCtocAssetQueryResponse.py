#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetDTO import AssetDTO


class AnttechNftCtocAssetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocAssetQueryResponse, self).__init__()
        self._asset_list = None
        self._has_more = None
        self._has_real_name = None
        self._last_index = None

    @property
    def asset_list(self):
        return self._asset_list

    @asset_list.setter
    def asset_list(self, value):
        if isinstance(value, list):
            self._asset_list = list()
            for i in value:
                if isinstance(i, AssetDTO):
                    self._asset_list.append(i)
                else:
                    self._asset_list.append(AssetDTO.from_alipay_dict(i))
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def has_real_name(self):
        return self._has_real_name

    @has_real_name.setter
    def has_real_name(self, value):
        self._has_real_name = value
    @property
    def last_index(self):
        return self._last_index

    @last_index.setter
    def last_index(self, value):
        self._last_index = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocAssetQueryResponse, self).parse_response_content(response_content)
        if 'asset_list' in response:
            self.asset_list = response['asset_list']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'has_real_name' in response:
            self.has_real_name = response['has_real_name']
        if 'last_index' in response:
            self.last_index = response['last_index']
