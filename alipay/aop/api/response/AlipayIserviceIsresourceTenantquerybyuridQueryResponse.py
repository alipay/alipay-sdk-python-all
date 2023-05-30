#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiTenantInfo import OpenApiTenantInfo


class AlipayIserviceIsresourceTenantquerybyuridQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIsresourceTenantquerybyuridQueryResponse, self).__init__()
        self._biz_data = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, list):
            self._biz_data = list()
            for i in value:
                if isinstance(i, OpenApiTenantInfo):
                    self._biz_data.append(i)
                else:
                    self._biz_data.append(OpenApiTenantInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIsresourceTenantquerybyuridQueryResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
