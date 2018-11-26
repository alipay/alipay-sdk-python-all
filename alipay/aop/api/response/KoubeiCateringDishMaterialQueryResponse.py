#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishMaterialInfo import KbdishMaterialInfo


class KoubeiCateringDishMaterialQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishMaterialQueryResponse, self).__init__()
        self._kb_dish_material_info_list = None
        self._page_no = None
        self._page_size = None
        self._total_count = None
        self._total_page = None

    @property
    def kb_dish_material_info_list(self):
        return self._kb_dish_material_info_list

    @kb_dish_material_info_list.setter
    def kb_dish_material_info_list(self, value):
        if isinstance(value, list):
            self._kb_dish_material_info_list = list()
            for i in value:
                if isinstance(i, KbdishMaterialInfo):
                    self._kb_dish_material_info_list.append(i)
                else:
                    self._kb_dish_material_info_list.append(KbdishMaterialInfo.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishMaterialQueryResponse, self).parse_response_content(response_content)
        if 'kb_dish_material_info_list' in response:
            self.kb_dish_material_info_list = response['kb_dish_material_info_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page' in response:
            self.total_page = response['total_page']
