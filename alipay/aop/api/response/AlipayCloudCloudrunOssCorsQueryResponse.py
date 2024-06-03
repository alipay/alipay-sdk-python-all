#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CorsSetting import CorsSetting


class AlipayCloudCloudrunOssCorsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunOssCorsQueryResponse, self).__init__()
        self._cors = None

    @property
    def cors(self):
        return self._cors

    @cors.setter
    def cors(self, value):
        if isinstance(value, CorsSetting):
            self._cors = value
        else:
            self._cors = CorsSetting.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunOssCorsQueryResponse, self).parse_response_content(response_content)
        if 'cors' in response:
            self.cors = response['cors']
