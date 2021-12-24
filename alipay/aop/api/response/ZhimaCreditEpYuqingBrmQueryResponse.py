#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NewsEntityAggregation import NewsEntityAggregation
from alipay.aop.api.domain.NewsSource import NewsSource
from alipay.aop.api.domain.NewsAggregationValue import NewsAggregationValue


class ZhimaCreditEpYuqingBrmQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpYuqingBrmQueryResponse, self).__init__()
        self._entity_aggregation = None
        self._hits = None
        self._label_aggregation = None
        self._total = None

    @property
    def entity_aggregation(self):
        return self._entity_aggregation

    @entity_aggregation.setter
    def entity_aggregation(self, value):
        if isinstance(value, NewsEntityAggregation):
            self._entity_aggregation = value
        else:
            self._entity_aggregation = NewsEntityAggregation.from_alipay_dict(value)
    @property
    def hits(self):
        return self._hits

    @hits.setter
    def hits(self, value):
        if isinstance(value, list):
            self._hits = list()
            for i in value:
                if isinstance(i, NewsSource):
                    self._hits.append(i)
                else:
                    self._hits.append(NewsSource.from_alipay_dict(i))
    @property
    def label_aggregation(self):
        return self._label_aggregation

    @label_aggregation.setter
    def label_aggregation(self, value):
        if isinstance(value, list):
            self._label_aggregation = list()
            for i in value:
                if isinstance(i, NewsAggregationValue):
                    self._label_aggregation.append(i)
                else:
                    self._label_aggregation.append(NewsAggregationValue.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpYuqingBrmQueryResponse, self).parse_response_content(response_content)
        if 'entity_aggregation' in response:
            self.entity_aggregation = response['entity_aggregation']
        if 'hits' in response:
            self.hits = response['hits']
        if 'label_aggregation' in response:
            self.label_aggregation = response['label_aggregation']
        if 'total' in response:
            self.total = response['total']
