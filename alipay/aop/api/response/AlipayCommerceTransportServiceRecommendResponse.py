#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TransportServiceRecommendItem import TransportServiceRecommendItem


class AlipayCommerceTransportServiceRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportServiceRecommendResponse, self).__init__()
        self._out_request_no = None
        self._request_trace_id = None
        self._service_list = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def request_trace_id(self):
        return self._request_trace_id

    @request_trace_id.setter
    def request_trace_id(self, value):
        self._request_trace_id = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, TransportServiceRecommendItem):
                    self._service_list.append(i)
                else:
                    self._service_list.append(TransportServiceRecommendItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportServiceRecommendResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'request_trace_id' in response:
            self.request_trace_id = response['request_trace_id']
        if 'service_list' in response:
            self.service_list = response['service_list']
