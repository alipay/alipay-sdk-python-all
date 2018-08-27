#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ModelMeta import ModelMeta


class AlipayMarketingDataModelBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingDataModelBatchqueryResponse, self).__init__()
        self._model_meta = None
        self._total_page_count = None

    @property
    def model_meta(self):
        return self._model_meta

    @model_meta.setter
    def model_meta(self, value):
        if isinstance(value, list):
            self._model_meta = list()
            for i in value:
                if isinstance(i, ModelMeta):
                    self._model_meta.append(i)
                else:
                    self._model_meta.append(ModelMeta.from_alipay_dict(i))
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingDataModelBatchqueryResponse, self).parse_response_content(response_content)
        if 'model_meta' in response:
            self.model_meta = response['model_meta']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
