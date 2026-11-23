#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CateringGoodInfo import CateringGoodInfo


class AlipayOpenSpNordercateringItemsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordercateringItemsQueryResponse, self).__init__()
        self._brand_action_url = None
        self._catering_goods = None
        self._expires_at = None
        self._exposed_item_list = None
        self._has_more = None
        self._identity_status = None
        self._session_id = None
        self._shop_detail_url = None

    @property
    def brand_action_url(self):
        return self._brand_action_url

    @brand_action_url.setter
    def brand_action_url(self, value):
        self._brand_action_url = value
    @property
    def catering_goods(self):
        return self._catering_goods

    @catering_goods.setter
    def catering_goods(self, value):
        if isinstance(value, list):
            self._catering_goods = list()
            for i in value:
                if isinstance(i, CateringGoodInfo):
                    self._catering_goods.append(i)
                else:
                    self._catering_goods.append(CateringGoodInfo.from_alipay_dict(i))
    @property
    def expires_at(self):
        return self._expires_at

    @expires_at.setter
    def expires_at(self, value):
        self._expires_at = value
    @property
    def exposed_item_list(self):
        return self._exposed_item_list

    @exposed_item_list.setter
    def exposed_item_list(self, value):
        self._exposed_item_list = value
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def identity_status(self):
        return self._identity_status

    @identity_status.setter
    def identity_status(self, value):
        self._identity_status = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def shop_detail_url(self):
        return self._shop_detail_url

    @shop_detail_url.setter
    def shop_detail_url(self, value):
        self._shop_detail_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordercateringItemsQueryResponse, self).parse_response_content(response_content)
        if 'brand_action_url' in response:
            self.brand_action_url = response['brand_action_url']
        if 'catering_goods' in response:
            self.catering_goods = response['catering_goods']
        if 'expires_at' in response:
            self.expires_at = response['expires_at']
        if 'exposed_item_list' in response:
            self.exposed_item_list = response['exposed_item_list']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'identity_status' in response:
            self.identity_status = response['identity_status']
        if 'session_id' in response:
            self.session_id = response['session_id']
        if 'shop_detail_url' in response:
            self.shop_detail_url = response['shop_detail_url']
