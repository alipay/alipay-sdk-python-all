#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LifeServiceShopBusinessTime import LifeServiceShopBusinessTime
from alipay.aop.api.domain.LifeServiceAttr import LifeServiceAttr


class AlipayCommerceLifeserviceShopdecorationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceShopdecorationQueryResponse, self).__init__()
        self._shop_business_time = None
        self._shop_commercial_tags = None
        self._shop_decoration_attrs = None
        self._shop_id = None
        self._shop_logo = None
        self._shop_vibes_images = None

    @property
    def shop_business_time(self):
        return self._shop_business_time

    @shop_business_time.setter
    def shop_business_time(self, value):
        if isinstance(value, list):
            self._shop_business_time = list()
            for i in value:
                if isinstance(i, LifeServiceShopBusinessTime):
                    self._shop_business_time.append(i)
                else:
                    self._shop_business_time.append(LifeServiceShopBusinessTime.from_alipay_dict(i))
    @property
    def shop_commercial_tags(self):
        return self._shop_commercial_tags

    @shop_commercial_tags.setter
    def shop_commercial_tags(self, value):
        if isinstance(value, list):
            self._shop_commercial_tags = list()
            for i in value:
                self._shop_commercial_tags.append(i)
    @property
    def shop_decoration_attrs(self):
        return self._shop_decoration_attrs

    @shop_decoration_attrs.setter
    def shop_decoration_attrs(self, value):
        if isinstance(value, list):
            self._shop_decoration_attrs = list()
            for i in value:
                if isinstance(i, LifeServiceAttr):
                    self._shop_decoration_attrs.append(i)
                else:
                    self._shop_decoration_attrs.append(LifeServiceAttr.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_logo(self):
        return self._shop_logo

    @shop_logo.setter
    def shop_logo(self, value):
        self._shop_logo = value
    @property
    def shop_vibes_images(self):
        return self._shop_vibes_images

    @shop_vibes_images.setter
    def shop_vibes_images(self, value):
        if isinstance(value, list):
            self._shop_vibes_images = list()
            for i in value:
                self._shop_vibes_images.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceShopdecorationQueryResponse, self).parse_response_content(response_content)
        if 'shop_business_time' in response:
            self.shop_business_time = response['shop_business_time']
        if 'shop_commercial_tags' in response:
            self.shop_commercial_tags = response['shop_commercial_tags']
        if 'shop_decoration_attrs' in response:
            self.shop_decoration_attrs = response['shop_decoration_attrs']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_logo' in response:
            self.shop_logo = response['shop_logo']
        if 'shop_vibes_images' in response:
            self.shop_vibes_images = response['shop_vibes_images']
