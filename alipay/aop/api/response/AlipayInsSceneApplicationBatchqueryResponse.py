#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsApplicationQuery import InsApplicationQuery


class AlipayInsSceneApplicationBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneApplicationBatchqueryResponse, self).__init__()
        self._applications = None

    @property
    def applications(self):
        return self._applications

    @applications.setter
    def applications(self, value):
        if isinstance(value, list):
            self._applications = list()
            for i in value:
                if isinstance(i, InsApplicationQuery):
                    self._applications.append(i)
                else:
                    self._applications.append(InsApplicationQuery.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneApplicationBatchqueryResponse, self).parse_response_content(response_content)
        if 'applications' in response:
            self.applications = response['applications']
