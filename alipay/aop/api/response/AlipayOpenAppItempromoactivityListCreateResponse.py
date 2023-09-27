#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemPromoActivityFailVO import ItemPromoActivityFailVO


class AlipayOpenAppItempromoactivityListCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItempromoactivityListCreateResponse, self).__init__()
        self._failed_item_list = None
        self._success_num = None
        self._total_num = None

    @property
    def failed_item_list(self):
        return self._failed_item_list

    @failed_item_list.setter
    def failed_item_list(self, value):
        if isinstance(value, list):
            self._failed_item_list = list()
            for i in value:
                if isinstance(i, ItemPromoActivityFailVO):
                    self._failed_item_list.append(i)
                else:
                    self._failed_item_list.append(ItemPromoActivityFailVO.from_alipay_dict(i))
    @property
    def success_num(self):
        return self._success_num

    @success_num.setter
    def success_num(self, value):
        self._success_num = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItempromoactivityListCreateResponse, self).parse_response_content(response_content)
        if 'failed_item_list' in response:
            self.failed_item_list = response['failed_item_list']
        if 'success_num' in response:
            self.success_num = response['success_num']
        if 'total_num' in response:
            self.total_num = response['total_num']
