#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MenuBean import MenuBean


class AlipayOfflineSmddShopCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddShopCategoryQueryResponse, self).__init__()
        self._menu_list = None

    @property
    def menu_list(self):
        return self._menu_list

    @menu_list.setter
    def menu_list(self, value):
        if isinstance(value, list):
            self._menu_list = list()
            for i in value:
                if isinstance(i, MenuBean):
                    self._menu_list.append(i)
                else:
                    self._menu_list.append(MenuBean.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddShopCategoryQueryResponse, self).parse_response_content(response_content)
        if 'menu_list' in response:
            self.menu_list = response['menu_list']
