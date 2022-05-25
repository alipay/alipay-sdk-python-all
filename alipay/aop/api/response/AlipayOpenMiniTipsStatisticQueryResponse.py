#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniTipsStatisticQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTipsStatisticQueryResponse, self).__init__()
        self._app_collect_cnt = None
        self._app_uv = None
        self._delivery_content = None
        self._delivery_id = None
        self._tips_collect_rate = None
        self._tips_collect_uv = None
        self._tips_expo_uv = None
        self._total_app_collect_cnt = None
        self._total_app_uv = None
        self._total_tips_collect_rate = None
        self._total_tips_collect_uv = None
        self._total_tips_expo_uv = None

    @property
    def app_collect_cnt(self):
        return self._app_collect_cnt

    @app_collect_cnt.setter
    def app_collect_cnt(self, value):
        self._app_collect_cnt = value
    @property
    def app_uv(self):
        return self._app_uv

    @app_uv.setter
    def app_uv(self, value):
        self._app_uv = value
    @property
    def delivery_content(self):
        return self._delivery_content

    @delivery_content.setter
    def delivery_content(self, value):
        self._delivery_content = value
    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def tips_collect_rate(self):
        return self._tips_collect_rate

    @tips_collect_rate.setter
    def tips_collect_rate(self, value):
        self._tips_collect_rate = value
    @property
    def tips_collect_uv(self):
        return self._tips_collect_uv

    @tips_collect_uv.setter
    def tips_collect_uv(self, value):
        self._tips_collect_uv = value
    @property
    def tips_expo_uv(self):
        return self._tips_expo_uv

    @tips_expo_uv.setter
    def tips_expo_uv(self, value):
        self._tips_expo_uv = value
    @property
    def total_app_collect_cnt(self):
        return self._total_app_collect_cnt

    @total_app_collect_cnt.setter
    def total_app_collect_cnt(self, value):
        self._total_app_collect_cnt = value
    @property
    def total_app_uv(self):
        return self._total_app_uv

    @total_app_uv.setter
    def total_app_uv(self, value):
        self._total_app_uv = value
    @property
    def total_tips_collect_rate(self):
        return self._total_tips_collect_rate

    @total_tips_collect_rate.setter
    def total_tips_collect_rate(self, value):
        self._total_tips_collect_rate = value
    @property
    def total_tips_collect_uv(self):
        return self._total_tips_collect_uv

    @total_tips_collect_uv.setter
    def total_tips_collect_uv(self, value):
        self._total_tips_collect_uv = value
    @property
    def total_tips_expo_uv(self):
        return self._total_tips_expo_uv

    @total_tips_expo_uv.setter
    def total_tips_expo_uv(self, value):
        self._total_tips_expo_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTipsStatisticQueryResponse, self).parse_response_content(response_content)
        if 'app_collect_cnt' in response:
            self.app_collect_cnt = response['app_collect_cnt']
        if 'app_uv' in response:
            self.app_uv = response['app_uv']
        if 'delivery_content' in response:
            self.delivery_content = response['delivery_content']
        if 'delivery_id' in response:
            self.delivery_id = response['delivery_id']
        if 'tips_collect_rate' in response:
            self.tips_collect_rate = response['tips_collect_rate']
        if 'tips_collect_uv' in response:
            self.tips_collect_uv = response['tips_collect_uv']
        if 'tips_expo_uv' in response:
            self.tips_expo_uv = response['tips_expo_uv']
        if 'total_app_collect_cnt' in response:
            self.total_app_collect_cnt = response['total_app_collect_cnt']
        if 'total_app_uv' in response:
            self.total_app_uv = response['total_app_uv']
        if 'total_tips_collect_rate' in response:
            self.total_tips_collect_rate = response['total_tips_collect_rate']
        if 'total_tips_collect_uv' in response:
            self.total_tips_collect_uv = response['total_tips_collect_uv']
        if 'total_tips_expo_uv' in response:
            self.total_tips_expo_uv = response['total_tips_expo_uv']
