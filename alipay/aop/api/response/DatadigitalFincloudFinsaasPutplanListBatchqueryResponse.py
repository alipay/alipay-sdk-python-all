#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChannelPutPlanDTO import ChannelPutPlanDTO


class DatadigitalFincloudFinsaasPutplanListBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasPutplanListBatchqueryResponse, self).__init__()
        self._list = None
        self._total = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, ChannelPutPlanDTO):
                    self._list.append(i)
                else:
                    self._list.append(ChannelPutPlanDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasPutplanListBatchqueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']
        if 'total' in response:
            self.total = response['total']
