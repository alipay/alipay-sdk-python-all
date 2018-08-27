#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DmActivityShopData import DmActivityShopData


class KoubeiMarketingDataRetailDmQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataRetailDmQueryResponse, self).__init__()
        self._content_id = None
        self._dm_marketing_datas = None
        self._item_code = None
        self._item_name = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def dm_marketing_datas(self):
        return self._dm_marketing_datas

    @dm_marketing_datas.setter
    def dm_marketing_datas(self, value):
        if isinstance(value, list):
            self._dm_marketing_datas = list()
            for i in value:
                if isinstance(i, DmActivityShopData):
                    self._dm_marketing_datas.append(i)
                else:
                    self._dm_marketing_datas.append(DmActivityShopData.from_alipay_dict(i))
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataRetailDmQueryResponse, self).parse_response_content(response_content)
        if 'content_id' in response:
            self.content_id = response['content_id']
        if 'dm_marketing_datas' in response:
            self.dm_marketing_datas = response['dm_marketing_datas']
        if 'item_code' in response:
            self.item_code = response['item_code']
        if 'item_name' in response:
            self.item_name = response['item_name']
