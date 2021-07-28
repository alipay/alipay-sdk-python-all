#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvTfjsModelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvTfjsModelQueryResponse, self).__init__()
        self._bin_url = None
        self._bin_urls = None
        self._model_json_url = None

    @property
    def bin_url(self):
        return self._bin_url

    @bin_url.setter
    def bin_url(self, value):
        self._bin_url = value
    @property
    def bin_urls(self):
        return self._bin_urls

    @bin_urls.setter
    def bin_urls(self, value):
        if isinstance(value, list):
            self._bin_urls = list()
            for i in value:
                self._bin_urls.append(i)
    @property
    def model_json_url(self):
        return self._model_json_url

    @model_json_url.setter
    def model_json_url(self, value):
        self._model_json_url = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvTfjsModelQueryResponse, self).parse_response_content(response_content)
        if 'bin_url' in response:
            self.bin_url = response['bin_url']
        if 'bin_urls' in response:
            self.bin_urls = response['bin_urls']
        if 'model_json_url' in response:
            self.model_json_url = response['model_json_url']
