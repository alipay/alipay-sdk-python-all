#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenSearchDocBO import OpenSearchDocBO


class DatadigitalFincloudFinsaasInsuranceOpensearchQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasInsuranceOpensearchQueryResponse, self).__init__()
        self._debug_info = None
        self._search_docs = None

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

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasInsuranceOpensearchQueryResponse, self).parse_response_content(response_content)
        if 'debug_info' in response:
            self.debug_info = response['debug_info']
        if 'search_docs' in response:
            self.search_docs = response['search_docs']
