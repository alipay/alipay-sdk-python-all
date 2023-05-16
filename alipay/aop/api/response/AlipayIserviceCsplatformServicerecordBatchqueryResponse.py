#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceRecordDetailVO import ServiceRecordDetailVO


class AlipayIserviceCsplatformServicerecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCsplatformServicerecordBatchqueryResponse, self).__init__()
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, list):
            self._value = list()
            for i in value:
                if isinstance(i, ServiceRecordDetailVO):
                    self._value.append(i)
                else:
                    self._value.append(ServiceRecordDetailVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCsplatformServicerecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'value' in response:
            self.value = response['value']
