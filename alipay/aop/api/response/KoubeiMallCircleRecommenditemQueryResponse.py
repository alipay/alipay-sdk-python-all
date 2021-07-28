#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CircleRecommendItemDTO import CircleRecommendItemDTO


class KoubeiMallCircleRecommenditemQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMallCircleRecommenditemQueryResponse, self).__init__()
        self._error_code = None
        self._error_msg = None
        self._has_more = None
        self._next_start = None
        self._page_size = None
        self._recommend_item = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def next_start(self):
        return self._next_start

    @next_start.setter
    def next_start(self, value):
        self._next_start = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def recommend_item(self):
        return self._recommend_item

    @recommend_item.setter
    def recommend_item(self, value):
        if isinstance(value, list):
            self._recommend_item = list()
            for i in value:
                if isinstance(i, CircleRecommendItemDTO):
                    self._recommend_item.append(i)
                else:
                    self._recommend_item.append(CircleRecommendItemDTO.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMallCircleRecommenditemQueryResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'next_start' in response:
            self.next_start = response['next_start']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'recommend_item' in response:
            self.recommend_item = response['recommend_item']
        if 'success' in response:
            self.success = response['success']
