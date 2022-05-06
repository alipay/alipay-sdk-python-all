#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryProfileDTO import QueryProfileDTO


class AlipayInsSceneInspetprodHasprofileBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInspetprodHasprofileBatchqueryResponse, self).__init__()
        self._model_list = None

    @property
    def model_list(self):
        return self._model_list

    @model_list.setter
    def model_list(self, value):
        if isinstance(value, list):
            self._model_list = list()
            for i in value:
                if isinstance(i, QueryProfileDTO):
                    self._model_list.append(i)
                else:
                    self._model_list.append(QueryProfileDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInspetprodHasprofileBatchqueryResponse, self).parse_response_content(response_content)
        if 'model_list' in response:
            self.model_list = response['model_list']
