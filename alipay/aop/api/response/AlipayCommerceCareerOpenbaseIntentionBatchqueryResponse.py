#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CareerOpenBaseIntentionLadarDetailResult import CareerOpenBaseIntentionLadarDetailResult


class AlipayCommerceCareerOpenbaseIntentionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCareerOpenbaseIntentionBatchqueryResponse, self).__init__()
        self._batch_details = None
        self._batch_no = None
        self._batch_status = None
        self._out_batch_no = None

    @property
    def batch_details(self):
        return self._batch_details

    @batch_details.setter
    def batch_details(self, value):
        if isinstance(value, list):
            self._batch_details = list()
            for i in value:
                if isinstance(i, CareerOpenBaseIntentionLadarDetailResult):
                    self._batch_details.append(i)
                else:
                    self._batch_details.append(CareerOpenBaseIntentionLadarDetailResult.from_alipay_dict(i))
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value
    @property
    def out_batch_no(self):
        return self._out_batch_no

    @out_batch_no.setter
    def out_batch_no(self, value):
        self._out_batch_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCareerOpenbaseIntentionBatchqueryResponse, self).parse_response_content(response_content)
        if 'batch_details' in response:
            self.batch_details = response['batch_details']
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'batch_status' in response:
            self.batch_status = response['batch_status']
        if 'out_batch_no' in response:
            self.out_batch_no = response['out_batch_no']
