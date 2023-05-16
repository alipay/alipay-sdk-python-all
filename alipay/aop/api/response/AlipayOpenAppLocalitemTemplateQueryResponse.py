#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemAttrGroupVO import ItemAttrGroupVO


class AlipayOpenAppLocalitemTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppLocalitemTemplateQueryResponse, self).__init__()
        self._attr = None
        self._category_id = None
        self._category_name = None
        self._item_type = None

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, value):
        if isinstance(value, ItemAttrGroupVO):
            self._attr = value
        else:
            self._attr = ItemAttrGroupVO.from_alipay_dict(value)
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppLocalitemTemplateQueryResponse, self).parse_response_content(response_content)
        if 'attr' in response:
            self.attr = response['attr']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'category_name' in response:
            self.category_name = response['category_name']
        if 'item_type' in response:
            self.item_type = response['item_type']
