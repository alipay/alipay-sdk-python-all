#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasDesignPageOfflineResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasDesignPageOfflineResponse, self).__init__()
        self._page_code = None

    @property
    def page_code(self):
        return self._page_code

    @page_code.setter
    def page_code(self, value):
        self._page_code = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasDesignPageOfflineResponse, self).parse_response_content(response_content)
        if 'page_code' in response:
            self.page_code = response['page_code']
