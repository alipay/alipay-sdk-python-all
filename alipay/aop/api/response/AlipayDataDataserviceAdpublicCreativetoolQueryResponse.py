#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserPublicQueryResponse import UserPublicQueryResponse


class AlipayDataDataserviceAdpublicCreativetoolQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdpublicCreativetoolQueryResponse, self).__init__()
        self._data_list = None
        self._total = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, UserPublicQueryResponse):
            self._data_list = value
        else:
            self._data_list = UserPublicQueryResponse.from_alipay_dict(value)
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdpublicCreativetoolQueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'total' in response:
            self.total = response['total']
