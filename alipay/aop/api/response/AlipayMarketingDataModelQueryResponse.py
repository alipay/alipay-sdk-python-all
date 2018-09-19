#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ModelColumn import ModelColumn


class AlipayMarketingDataModelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingDataModelQueryResponse, self).__init__()
        self._model_column = None

    @property
    def model_column(self):
        return self._model_column

    @model_column.setter
    def model_column(self, value):
        if isinstance(value, list):
            self._model_column = list()
            for i in value:
                if isinstance(i, ModelColumn):
                    self._model_column.append(i)
                else:
                    self._model_column.append(ModelColumn.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingDataModelQueryResponse, self).parse_response_content(response_content)
        if 'model_column' in response:
            self.model_column = response['model_column']
