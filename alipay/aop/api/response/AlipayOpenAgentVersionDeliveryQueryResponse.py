#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentVersionDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentVersionDeliveryQueryResponse, self).__init__()
        self._delivery_id = None
        self._delivery_status = None
        self._reject_reason = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentVersionDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'delivery_id' in response:
            self.delivery_id = response['delivery_id']
        if 'delivery_status' in response:
            self.delivery_status = response['delivery_status']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
