#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineNbinteractSceneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineNbinteractSceneQueryResponse, self).__init__()
        self._bind_status = None
        self._bind_time = None
        self._link_url = None
        self._sn = None
        self._url_type = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def bind_time(self):
        return self._bind_time

    @bind_time.setter
    def bind_time(self, value):
        self._bind_time = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def url_type(self):
        return self._url_type

    @url_type.setter
    def url_type(self, value):
        self._url_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineNbinteractSceneQueryResponse, self).parse_response_content(response_content)
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'bind_time' in response:
            self.bind_time = response['bind_time']
        if 'link_url' in response:
            self.link_url = response['link_url']
        if 'sn' in response:
            self.sn = response['sn']
        if 'url_type' in response:
            self.url_type = response['url_type']
