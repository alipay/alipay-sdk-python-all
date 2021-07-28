#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMultimediaXnnminiModelCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMultimediaXnnminiModelCreateResponse, self).__init__()
        self._model_id = None

    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMultimediaXnnminiModelCreateResponse, self).parse_response_content(response_content)
        if 'model_id' in response:
            self.model_id = response['model_id']
