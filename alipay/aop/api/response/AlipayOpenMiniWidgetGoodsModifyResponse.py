#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniWidgetGoodsModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniWidgetGoodsModifyResponse, self).__init__()
        self._commit_id = None

    @property
    def commit_id(self):
        return self._commit_id

    @commit_id.setter
    def commit_id(self, value):
        self._commit_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniWidgetGoodsModifyResponse, self).parse_response_content(response_content)
        if 'commit_id' in response:
            self.commit_id = response['commit_id']
