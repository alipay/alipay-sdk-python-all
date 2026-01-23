#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantNdata import MerchantNdata


class AlipayMerchantNtooldataDayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantNtooldataDayQueryResponse, self).__init__()
        self._data = None
        self._device_type = None
        self._metrics_date = None
        self._page_num = None
        self._page_size = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, MerchantNdata):
                    self._data.append(i)
                else:
                    self._data.append(MerchantNdata.from_alipay_dict(i))
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def metrics_date(self):
        return self._metrics_date

    @metrics_date.setter
    def metrics_date(self, value):
        self._metrics_date = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantNtooldataDayQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'device_type' in response:
            self.device_type = response['device_type']
        if 'metrics_date' in response:
            self.metrics_date = response['metrics_date']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
