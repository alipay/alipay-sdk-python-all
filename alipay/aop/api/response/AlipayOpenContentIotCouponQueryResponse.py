#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenContentIotCouponQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenContentIotCouponQueryResponse, self).__init__()
        self._btn_act = None
        self._camp_id = None
        self._component_template = None
        self._content = None
        self._item_type = None
        self._nonempty_coupon_list = None
        self._prize_type = None
        self._shop_info = None
        self._url = None
        self._voice_broadcast = None

    @property
    def btn_act(self):
        return self._btn_act

    @btn_act.setter
    def btn_act(self, value):
        self._btn_act = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def component_template(self):
        return self._component_template

    @component_template.setter
    def component_template(self, value):
        self._component_template = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def nonempty_coupon_list(self):
        return self._nonempty_coupon_list

    @nonempty_coupon_list.setter
    def nonempty_coupon_list(self, value):
        self._nonempty_coupon_list = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        self._shop_info = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def voice_broadcast(self):
        return self._voice_broadcast

    @voice_broadcast.setter
    def voice_broadcast(self, value):
        self._voice_broadcast = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenContentIotCouponQueryResponse, self).parse_response_content(response_content)
        if 'btn_act' in response:
            self.btn_act = response['btn_act']
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'component_template' in response:
            self.component_template = response['component_template']
        if 'content' in response:
            self.content = response['content']
        if 'item_type' in response:
            self.item_type = response['item_type']
        if 'nonempty_coupon_list' in response:
            self.nonempty_coupon_list = response['nonempty_coupon_list']
        if 'prize_type' in response:
            self.prize_type = response['prize_type']
        if 'shop_info' in response:
            self.shop_info = response['shop_info']
        if 'url' in response:
            self.url = response['url']
        if 'voice_broadcast' in response:
            self.voice_broadcast = response['voice_broadcast']
