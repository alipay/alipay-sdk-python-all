#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Layer import Layer


class AlipayCloudCloudbaseLayerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseLayerQueryResponse, self).__init__()
        self._layers = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def layers(self):
        return self._layers

    @layers.setter
    def layers(self, value):
        if isinstance(value, list):
            self._layers = list()
            for i in value:
                if isinstance(i, Layer):
                    self._layers.append(i)
                else:
                    self._layers.append(Layer.from_alipay_dict(i))
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseLayerQueryResponse, self).parse_response_content(response_content)
        if 'layers' in response:
            self.layers = response['layers']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
