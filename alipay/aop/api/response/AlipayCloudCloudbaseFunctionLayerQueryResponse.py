#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LayerInfo import LayerInfo


class AlipayCloudCloudbaseFunctionLayerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionLayerQueryResponse, self).__init__()
        self._layers = None

    @property
    def layers(self):
        return self._layers

    @layers.setter
    def layers(self, value):
        if isinstance(value, list):
            self._layers = list()
            for i in value:
                if isinstance(i, LayerInfo):
                    self._layers.append(i)
                else:
                    self._layers.append(LayerInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionLayerQueryResponse, self).parse_response_content(response_content)
        if 'layers' in response:
            self.layers = response['layers']
