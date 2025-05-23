#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenXlightCrowd import OpenXlightCrowd


class AlipayDataDataserviceAdcrowdDmpcrowdBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcrowdDmpcrowdBatchqueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, OpenXlightCrowd):
                    self._data.append(i)
                else:
                    self._data.append(OpenXlightCrowd.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcrowdDmpcrowdBatchqueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
