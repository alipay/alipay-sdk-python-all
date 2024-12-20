#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPayafteruseFulfillmentorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseFulfillmentorderQueryResponse, self).__init__()
        self._fulfillment = None
        self._fulfillment_status = None
        self._overdue = None

    @property
    def fulfillment(self):
        return self._fulfillment

    @fulfillment.setter
    def fulfillment(self, value):
        self._fulfillment = value
    @property
    def fulfillment_status(self):
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, value):
        self._fulfillment_status = value
    @property
    def overdue(self):
        return self._overdue

    @overdue.setter
    def overdue(self, value):
        self._overdue = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPayafteruseFulfillmentorderQueryResponse, self).parse_response_content(response_content)
        if 'fulfillment' in response:
            self.fulfillment = response['fulfillment']
        if 'fulfillment_status' in response:
            self.fulfillment_status = response['fulfillment_status']
        if 'overdue' in response:
            self.overdue = response['overdue']
