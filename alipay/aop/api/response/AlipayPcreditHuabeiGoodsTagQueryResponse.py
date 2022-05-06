#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GoodsTagResult import GoodsTagResult


class AlipayPcreditHuabeiGoodsTagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiGoodsTagQueryResponse, self).__init__()
        self._success = None
        self._tags = None

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                if isinstance(i, GoodsTagResult):
                    self._tags.append(i)
                else:
                    self._tags.append(GoodsTagResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiGoodsTagQueryResponse, self).parse_response_content(response_content)
        if 'success' in response:
            self.success = response['success']
        if 'tags' in response:
            self.tags = response['tags']
