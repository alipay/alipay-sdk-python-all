#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MaterialResultInfo import MaterialResultInfo
from alipay.aop.api.domain.MaterialResultInfo import MaterialResultInfo


class AlipayDigitalopUcdpApecreativePictaskresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalopUcdpApecreativePictaskresultQueryResponse, self).__init__()
        self._material_result_info_list = None
        self._material_result_list = None

    @property
    def material_result_info_list(self):
        return self._material_result_info_list

    @material_result_info_list.setter
    def material_result_info_list(self, value):
        if isinstance(value, MaterialResultInfo):
            self._material_result_info_list = value
        else:
            self._material_result_info_list = MaterialResultInfo.from_alipay_dict(value)
    @property
    def material_result_list(self):
        return self._material_result_list

    @material_result_list.setter
    def material_result_list(self, value):
        if isinstance(value, list):
            self._material_result_list = list()
            for i in value:
                if isinstance(i, MaterialResultInfo):
                    self._material_result_list.append(i)
                else:
                    self._material_result_list.append(MaterialResultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalopUcdpApecreativePictaskresultQueryResponse, self).parse_response_content(response_content)
        if 'material_result_info_list' in response:
            self.material_result_info_list = response['material_result_info_list']
        if 'material_result_list' in response:
            self.material_result_list = response['material_result_list']
