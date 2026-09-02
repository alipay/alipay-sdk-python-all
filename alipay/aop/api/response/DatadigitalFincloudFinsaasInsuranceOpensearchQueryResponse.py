#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenSearchDocBO import OpenSearchDocBO
from alipay.aop.api.domain.OpenSearchImageBO import OpenSearchImageBO


class DatadigitalFincloudFinsaasInsuranceOpensearchQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasInsuranceOpensearchQueryResponse, self).__init__()
        self._debug_info = None
        self._search_docs = None
        self._search_images = None

    @property
    def debug_info(self):
        return self._debug_info

    @debug_info.setter
    def debug_info(self, value):
        self._debug_info = value
    @property
    def search_docs(self):
        return self._search_docs

    @search_docs.setter
    def search_docs(self, value):
        if isinstance(value, list):
            self._search_docs = list()
            for i in value:
                if isinstance(i, OpenSearchDocBO):
                    self._search_docs.append(i)
                else:
                    self._search_docs.append(OpenSearchDocBO.from_alipay_dict(i))
    @property
    def search_images(self):
        return self._search_images

    @search_images.setter
    def search_images(self, value):
        if isinstance(value, list):
            self._search_images = list()
            for i in value:
                if isinstance(i, OpenSearchImageBO):
                    self._search_images.append(i)
                else:
                    self._search_images.append(OpenSearchImageBO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasInsuranceOpensearchQueryResponse, self).parse_response_content(response_content)
        if 'debug_info' in response:
            self.debug_info = response['debug_info']
        if 'search_docs' in response:
            self.search_docs = response['search_docs']
        if 'search_images' in response:
            self.search_images = response['search_images']
