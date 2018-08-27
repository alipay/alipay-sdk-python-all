#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneMarketingContentGroup import SceneMarketingContentGroup
from alipay.aop.api.domain.SceneMarketingHeader import SceneMarketingHeader


class KoubeiMarketingDataSceneTravelGetResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataSceneTravelGetResponse, self).__init__()
        self._content = None
        self._header = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content = list()
            for i in value:
                if isinstance(i, SceneMarketingContentGroup):
                    self._content.append(i)
                else:
                    self._content.append(SceneMarketingContentGroup.from_alipay_dict(i))
    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        if isinstance(value, SceneMarketingHeader):
            self._header = value
        else:
            self._header = SceneMarketingHeader.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataSceneTravelGetResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'header' in response:
            self.header = response['header']
