#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoAigcOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAigcOrderQueryResponse, self).__init__()
        self._desc = None
        self._images = None
        self._status = None
        self._texts = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def texts(self):
        return self._texts

    @texts.setter
    def texts(self, value):
        if isinstance(value, list):
            self._texts = list()
            for i in value:
                self._texts.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAigcOrderQueryResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
        if 'images' in response:
            self.images = response['images']
        if 'status' in response:
            self.status = response['status']
        if 'texts' in response:
            self.texts = response['texts']
