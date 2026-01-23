#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationShangouStoreandgoodsRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationShangouStoreandgoodsRecommendResponse, self).__init__()
        self._action_url = None
        self._result_data = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        self._result_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationShangouStoreandgoodsRecommendResponse, self).parse_response_content(response_content)
        if 'action_url' in response:
            self.action_url = response['action_url']
        if 'result_data' in response:
            self.result_data = response['result_data']
