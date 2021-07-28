#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IotContentModuleInfo import IotContentModuleInfo


class AlipayMarketingIotBoothQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingIotBoothQueryResponse, self).__init__()
        self._booth_token = None
        self._content_list = None
        self._engine_type = None
        self._usable = None

    @property
    def booth_token(self):
        return self._booth_token

    @booth_token.setter
    def booth_token(self, value):
        self._booth_token = value
    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                if isinstance(i, IotContentModuleInfo):
                    self._content_list.append(i)
                else:
                    self._content_list.append(IotContentModuleInfo.from_alipay_dict(i))
    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, value):
        self._engine_type = value
    @property
    def usable(self):
        return self._usable

    @usable.setter
    def usable(self, value):
        self._usable = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingIotBoothQueryResponse, self).parse_response_content(response_content)
        if 'booth_token' in response:
            self.booth_token = response['booth_token']
        if 'content_list' in response:
            self.content_list = response['content_list']
        if 'engine_type' in response:
            self.engine_type = response['engine_type']
        if 'usable' in response:
            self.usable = response['usable']
