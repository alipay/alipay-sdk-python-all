#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppModelQueryResponse import MiniAppModelQueryResponse


class AlipayOpenMiniModelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniModelQueryResponse, self).__init__()
        self._model_infos = None

    @property
    def model_infos(self):
        return self._model_infos

    @model_infos.setter
    def model_infos(self, value):
        if isinstance(value, list):
            self._model_infos = list()
            for i in value:
                if isinstance(i, MiniAppModelQueryResponse):
                    self._model_infos.append(i)
                else:
                    self._model_infos.append(MiniAppModelQueryResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniModelQueryResponse, self).parse_response_content(response_content)
        if 'model_infos' in response:
            self.model_infos = response['model_infos']
