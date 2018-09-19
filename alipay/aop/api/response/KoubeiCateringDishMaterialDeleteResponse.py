#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishMaterialInfo import KbdishMaterialInfo


class KoubeiCateringDishMaterialDeleteResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishMaterialDeleteResponse, self).__init__()
        self._kb_dish_material_info = None

    @property
    def kb_dish_material_info(self):
        return self._kb_dish_material_info

    @kb_dish_material_info.setter
    def kb_dish_material_info(self, value):
        if isinstance(value, KbdishMaterialInfo):
            self._kb_dish_material_info = value
        else:
            self._kb_dish_material_info = KbdishMaterialInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishMaterialDeleteResponse, self).parse_response_content(response_content)
        if 'kb_dish_material_info' in response:
            self.kb_dish_material_info = response['kb_dish_material_info']
