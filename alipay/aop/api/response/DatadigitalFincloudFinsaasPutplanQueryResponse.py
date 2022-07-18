#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChannelPutPlanDetailDTO import ChannelPutPlanDetailDTO


class DatadigitalFincloudFinsaasPutplanQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasPutplanQueryResponse, self).__init__()
        self._detail = None

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        if isinstance(value, ChannelPutPlanDetailDTO):
            self._detail = value
        else:
            self._detail = ChannelPutPlanDetailDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasPutplanQueryResponse, self).parse_response_content(response_content)
        if 'detail' in response:
            self.detail = response['detail']
