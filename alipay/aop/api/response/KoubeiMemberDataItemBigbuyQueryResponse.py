#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndexBigbuyItem import IndexBigbuyItem
from alipay.aop.api.domain.IndexBlockBanner import IndexBlockBanner


class KoubeiMemberDataItemBigbuyQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMemberDataItemBigbuyQueryResponse, self).__init__()
        self._big_buy_item_list = None
        self._current_time = None
        self._gmt_end = None
        self._gmt_start = None
        self._index_block_banner = None
        self._promo_schema = None

    @property
    def big_buy_item_list(self):
        return self._big_buy_item_list

    @big_buy_item_list.setter
    def big_buy_item_list(self, value):
        if isinstance(value, list):
            self._big_buy_item_list = list()
            for i in value:
                if isinstance(i, IndexBigbuyItem):
                    self._big_buy_item_list.append(i)
                else:
                    self._big_buy_item_list.append(IndexBigbuyItem.from_alipay_dict(i))
    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, value):
        self._current_time = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def index_block_banner(self):
        return self._index_block_banner

    @index_block_banner.setter
    def index_block_banner(self, value):
        if isinstance(value, IndexBlockBanner):
            self._index_block_banner = value
        else:
            self._index_block_banner = IndexBlockBanner.from_alipay_dict(value)
    @property
    def promo_schema(self):
        return self._promo_schema

    @promo_schema.setter
    def promo_schema(self, value):
        self._promo_schema = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMemberDataItemBigbuyQueryResponse, self).parse_response_content(response_content)
        if 'big_buy_item_list' in response:
            self.big_buy_item_list = response['big_buy_item_list']
        if 'current_time' in response:
            self.current_time = response['current_time']
        if 'gmt_end' in response:
            self.gmt_end = response['gmt_end']
        if 'gmt_start' in response:
            self.gmt_start = response['gmt_start']
        if 'index_block_banner' in response:
            self.index_block_banner = response['index_block_banner']
        if 'promo_schema' in response:
            self.promo_schema = response['promo_schema']
