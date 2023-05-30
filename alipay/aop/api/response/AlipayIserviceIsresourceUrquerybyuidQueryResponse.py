#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiUserResourceInfo import OpenApiUserResourceInfo


class AlipayIserviceIsresourceUrquerybyuidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIsresourceUrquerybyuidQueryResponse, self).__init__()
        self._biz_data = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, OpenApiUserResourceInfo):
            self._biz_data = value
        else:
            self._biz_data = OpenApiUserResourceInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIsresourceUrquerybyuidQueryResponse, self).parse_response_content(response_content)
        if 'biz_data' in response:
            self.biz_data = response['biz_data']
