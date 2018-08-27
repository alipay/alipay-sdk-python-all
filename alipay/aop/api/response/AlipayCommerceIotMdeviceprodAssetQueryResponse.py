#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMdeviceprodAssetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMdeviceprodAssetQueryResponse, self).__init__()
        self._image_url = None
        self._item_name = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMdeviceprodAssetQueryResponse, self).parse_response_content(response_content)
        if 'image_url' in response:
            self.image_url = response['image_url']
        if 'item_name' in response:
            self.item_name = response['item_name']
