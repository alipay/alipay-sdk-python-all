#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiTenantInfo import OpenApiTenantInfo


class AlipayIserviceIsresourceTenantquerybytntidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIsresourceTenantquerybytntidQueryResponse, self).__init__()
        self._biz_data = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, OpenApiTenantInfo):
            self._biz_data = value
        else:
            self._biz_data = OpenApiTenantInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIsresourceTenantquerybytntidQueryResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
