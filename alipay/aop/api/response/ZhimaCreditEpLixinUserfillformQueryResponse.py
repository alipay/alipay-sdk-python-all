#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RightsFormItemValues import RightsFormItemValues


class ZhimaCreditEpLixinUserfillformQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpLixinUserfillformQueryResponse, self).__init__()
        self._has_next = None
        self._item_list = None
        self._page_index = None
        self._page_total = None
        self._rights_id = None
        self._rights_name = None
        self._total = None

    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, RightsFormItemValues):
                    self._item_list.append(i)
                else:
                    self._item_list.append(RightsFormItemValues.from_alipay_dict(i))
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_total(self):
        return self._page_total

    @page_total.setter
    def page_total(self, value):
        self._page_total = value
    @property
    def rights_id(self):
        return self._rights_id

    @rights_id.setter
    def rights_id(self, value):
        self._rights_id = value
    @property
    def rights_name(self):
        return self._rights_name

    @rights_name.setter
    def rights_name(self, value):
        self._rights_name = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpLixinUserfillformQueryResponse, self).parse_response_content(response_content)
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_total' in response:
            self.page_total = response['page_total']
        if 'rights_id' in response:
            self.rights_id = response['rights_id']
        if 'rights_name' in response:
            self.rights_name = response['rights_name']
        if 'total' in response:
            self.total = response['total']
