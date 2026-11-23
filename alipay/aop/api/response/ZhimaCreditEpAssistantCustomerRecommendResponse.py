#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CustomerRecommendation import CustomerRecommendation


class ZhimaCreditEpAssistantCustomerRecommendResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAssistantCustomerRecommendResponse, self).__init__()
        self._data_as_of = None
        self._generated_at = None
        self._recommendation_batch_id = None
        self._recommendations = None
        self._retry_after_ms = None
        self._status = None

    @property
    def data_as_of(self):
        return self._data_as_of

    @data_as_of.setter
    def data_as_of(self, value):
        self._data_as_of = value
    @property
    def generated_at(self):
        return self._generated_at

    @generated_at.setter
    def generated_at(self, value):
        self._generated_at = value
    @property
    def recommendation_batch_id(self):
        return self._recommendation_batch_id

    @recommendation_batch_id.setter
    def recommendation_batch_id(self, value):
        self._recommendation_batch_id = value
    @property
    def recommendations(self):
        return self._recommendations

    @recommendations.setter
    def recommendations(self, value):
        if isinstance(value, list):
            self._recommendations = list()
            for i in value:
                if isinstance(i, CustomerRecommendation):
                    self._recommendations.append(i)
                else:
                    self._recommendations.append(CustomerRecommendation.from_alipay_dict(i))
    @property
    def retry_after_ms(self):
        return self._retry_after_ms

    @retry_after_ms.setter
    def retry_after_ms(self, value):
        self._retry_after_ms = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAssistantCustomerRecommendResponse, self).parse_response_content(response_content)
        if 'data_as_of' in response:
            self.data_as_of = response['data_as_of']
        if 'generated_at' in response:
            self.generated_at = response['generated_at']
        if 'recommendation_batch_id' in response:
            self.recommendation_batch_id = response['recommendation_batch_id']
        if 'recommendations' in response:
            self.recommendations = response['recommendations']
        if 'retry_after_ms' in response:
            self.retry_after_ms = response['retry_after_ms']
        if 'status' in response:
            self.status = response['status']
