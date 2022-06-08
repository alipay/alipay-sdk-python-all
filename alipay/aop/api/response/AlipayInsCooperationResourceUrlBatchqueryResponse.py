#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResourceRelatedItem import ResourceRelatedItem


class AlipayInsCooperationResourceUrlBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsCooperationResourceUrlBatchqueryResponse, self).__init__()
        self._resource_items = None
        self._response_time = None
        self._result_code = None
        self._result_desc = None

    @property
    def resource_items(self):
        return self._resource_items

    @resource_items.setter
    def resource_items(self, value):
        if isinstance(value, list):
            self._resource_items = list()
            for i in value:
                if isinstance(i, ResourceRelatedItem):
                    self._resource_items.append(i)
                else:
                    self._resource_items.append(ResourceRelatedItem.from_alipay_dict(i))
    @property
    def response_time(self):
        return self._response_time

    @response_time.setter
    def response_time(self, value):
        self._response_time = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsCooperationResourceUrlBatchqueryResponse, self).parse_response_content(response_content)
        if 'resource_items' in response:
            self.resource_items = response['resource_items']
        if 'response_time' in response:
            self.response_time = response['response_time']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
