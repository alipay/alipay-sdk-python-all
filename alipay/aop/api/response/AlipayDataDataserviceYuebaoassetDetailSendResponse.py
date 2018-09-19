#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceYuebaoassetDetailSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceYuebaoassetDetailSendResponse, self).__init__()
        self._yeb_asset_data_num = None

    @property
    def yeb_asset_data_num(self):
        return self._yeb_asset_data_num

    @yeb_asset_data_num.setter
    def yeb_asset_data_num(self, value):
        self._yeb_asset_data_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceYuebaoassetDetailSendResponse, self).parse_response_content(response_content)
        if 'yeb_asset_data_num' in response:
            self.yeb_asset_data_num = response['yeb_asset_data_num']
