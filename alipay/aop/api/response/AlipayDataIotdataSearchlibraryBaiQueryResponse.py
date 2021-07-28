#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataIotdataSearchlibraryBaiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataIotdataSearchlibraryBaiQueryResponse, self).__init__()
        self._model_info = None
        self._repeat_info = None
        self._similarity_info = None

    @property
    def model_info(self):
        return self._model_info

    @model_info.setter
    def model_info(self, value):
        self._model_info = value
    @property
    def repeat_info(self):
        return self._repeat_info

    @repeat_info.setter
    def repeat_info(self, value):
        self._repeat_info = value
    @property
    def similarity_info(self):
        return self._similarity_info

    @similarity_info.setter
    def similarity_info(self, value):
        self._similarity_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataIotdataSearchlibraryBaiQueryResponse, self).parse_response_content(response_content)
        if 'model_info' in response:
            self.model_info = response['model_info']
        if 'repeat_info' in response:
            self.repeat_info = response['repeat_info']
        if 'similarity_info' in response:
            self.similarity_info = response['similarity_info']
