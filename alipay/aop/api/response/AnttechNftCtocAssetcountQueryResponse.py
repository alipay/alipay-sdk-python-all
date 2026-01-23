#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftCtocAssetcountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocAssetcountQueryResponse, self).__init__()
        self._dt = None
        self._total_owned_asset_num = None

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def total_owned_asset_num(self):
        return self._total_owned_asset_num

    @total_owned_asset_num.setter
    def total_owned_asset_num(self, value):
        self._total_owned_asset_num = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocAssetcountQueryResponse, self).parse_response_content(response_content)
        if 'dt' in response:
            self.dt = response['dt']
        if 'total_owned_asset_num' in response:
            self.total_owned_asset_num = response['total_owned_asset_num']
