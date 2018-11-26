#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MaterialEntity import MaterialEntity


class KoubeiCateringPosMaterialQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosMaterialQueryResponse, self).__init__()
        self._material_entity_list = None

    @property
    def material_entity_list(self):
        return self._material_entity_list

    @material_entity_list.setter
    def material_entity_list(self, value):
        if isinstance(value, list):
            self._material_entity_list = list()
            for i in value:
                if isinstance(i, MaterialEntity):
                    self._material_entity_list.append(i)
                else:
                    self._material_entity_list.append(MaterialEntity.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosMaterialQueryResponse, self).parse_response_content(response_content)
        if 'material_entity_list' in response:
            self.material_entity_list = response['material_entity_list']
