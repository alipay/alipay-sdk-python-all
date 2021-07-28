#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUserScenePreconsultResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserScenePreconsultResponse, self).__init__()
        self._accessible = None
        self._available_amount = None
        self._available_goods_count = None
        self._buyer_id = None
        self._eval_invoke_id = None
        self._scene_level = None
        self._top_amount = None
        self._top_goods_count = None

    @property
    def accessible(self):
        return self._accessible

    @accessible.setter
    def accessible(self, value):
        self._accessible = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def available_goods_count(self):
        return self._available_goods_count

    @available_goods_count.setter
    def available_goods_count(self, value):
        self._available_goods_count = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def eval_invoke_id(self):
        return self._eval_invoke_id

    @eval_invoke_id.setter
    def eval_invoke_id(self, value):
        self._eval_invoke_id = value
    @property
    def scene_level(self):
        return self._scene_level

    @scene_level.setter
    def scene_level(self, value):
        self._scene_level = value
    @property
    def top_amount(self):
        return self._top_amount

    @top_amount.setter
    def top_amount(self, value):
        self._top_amount = value
    @property
    def top_goods_count(self):
        return self._top_goods_count

    @top_goods_count.setter
    def top_goods_count(self, value):
        self._top_goods_count = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserScenePreconsultResponse, self).parse_response_content(response_content)
        if 'accessible' in response:
            self.accessible = response['accessible']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'available_goods_count' in response:
            self.available_goods_count = response['available_goods_count']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'eval_invoke_id' in response:
            self.eval_invoke_id = response['eval_invoke_id']
        if 'scene_level' in response:
            self.scene_level = response['scene_level']
        if 'top_amount' in response:
            self.top_amount = response['top_amount']
        if 'top_goods_count' in response:
            self.top_goods_count = response['top_goods_count']
