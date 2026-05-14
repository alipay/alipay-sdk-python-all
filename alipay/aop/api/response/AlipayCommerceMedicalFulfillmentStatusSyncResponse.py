#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalFulfillmentStatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalFulfillmentStatusSyncResponse, self).__init__()
        self._fulfillment_id = None

    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalFulfillmentStatusSyncResponse, self).parse_response_content(response_content)
        if 'fulfillment_id' in response:
            self.fulfillment_id = response['fulfillment_id']
