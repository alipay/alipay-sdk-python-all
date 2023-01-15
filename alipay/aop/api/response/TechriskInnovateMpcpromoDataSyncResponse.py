#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcpromoGoodsList import MpcpromoGoodsList


class TechriskInnovateMpcpromoDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoDataSyncResponse, self).__init__()
        self._data_list = None
        self._trace_id = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, MpcpromoGoodsList):
            self._data_list = value
        else:
            self._data_list = MpcpromoGoodsList.from_alipay_dict(value)
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoDataSyncResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
