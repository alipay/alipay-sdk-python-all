#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneCategoryDTO import SceneCategoryDTO


class AlipayMerchantSolcreditserviceprodScenecategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodScenecategoryQueryResponse, self).__init__()
        self._scene_category_list = None

    @property
    def scene_category_list(self):
        return self._scene_category_list

    @scene_category_list.setter
    def scene_category_list(self, value):
        if isinstance(value, list):
            self._scene_category_list = list()
            for i in value:
                if isinstance(i, SceneCategoryDTO):
                    self._scene_category_list.append(i)
                else:
                    self._scene_category_list.append(SceneCategoryDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodScenecategoryQueryResponse, self).parse_response_content(response_content)
        if 'scene_category_list' in response:
            self.scene_category_list = response['scene_category_list']
