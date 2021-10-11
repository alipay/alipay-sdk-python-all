#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmpeExpressQueryResponse import AmpeExpressQueryResponse


class AlipayOpenMiniAmpeExpressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeExpressQueryResponse, self).__init__()
        self._data = None
        self._logo = None
        self._merchant_detail_url = None
        self._mini_app_id = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, AmpeExpressQueryResponse):
                    self._data.append(i)
                else:
                    self._data.append(AmpeExpressQueryResponse.from_alipay_dict(i))
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def merchant_detail_url(self):
        return self._merchant_detail_url

    @merchant_detail_url.setter
    def merchant_detail_url(self, value):
        self._merchant_detail_url = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeExpressQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'logo' in response:
            self.logo = response['logo']
        if 'merchant_detail_url' in response:
            self.merchant_detail_url = response['merchant_detail_url']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
