#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CateInfoVO import CateInfoVO
from alipay.aop.api.domain.ItemInfoVO import ItemInfoVO
from alipay.aop.api.domain.CateInfoVO import CateInfoVO


class AlipayCommerceEducateTrainRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateTrainRecommendQueryResponse, self).__init__()
        self._default_first_cate = None
        self._has_more = None
        self._item_infos = None
        self._selected_first_cate = None

    @property
    def default_first_cate(self):
        return self._default_first_cate

    @default_first_cate.setter
    def default_first_cate(self, value):
        if isinstance(value, CateInfoVO):
            self._default_first_cate = value
        else:
            self._default_first_cate = CateInfoVO.from_alipay_dict(value)
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, ItemInfoVO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(ItemInfoVO.from_alipay_dict(i))
    @property
    def selected_first_cate(self):
        return self._selected_first_cate

    @selected_first_cate.setter
    def selected_first_cate(self, value):
        if isinstance(value, CateInfoVO):
            self._selected_first_cate = value
        else:
            self._selected_first_cate = CateInfoVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateTrainRecommendQueryResponse, self).parse_response_content(response_content)
        if 'default_first_cate' in response:
            self.default_first_cate = response['default_first_cate']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'item_infos' in response:
            self.item_infos = response['item_infos']
        if 'selected_first_cate' in response:
            self.selected_first_cate = response['selected_first_cate']
