#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAnttechWeatherHistoryforecastQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechWeatherHistoryforecastQueryResponse, self).__init__()
        self._data_ready = None
        self._download_url = None
        self._request_id = None
        self._url_expires_at = None

    @property
    def data_ready(self):
        return self._data_ready

    @data_ready.setter
    def data_ready(self, value):
        self._data_ready = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def url_expires_at(self):
        return self._url_expires_at

    @url_expires_at.setter
    def url_expires_at(self, value):
        self._url_expires_at = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechWeatherHistoryforecastQueryResponse, self).parse_response_content(response_content)
        if 'data_ready' in response:
            self.data_ready = response['data_ready']
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'url_expires_at' in response:
            self.url_expires_at = response['url_expires_at']
