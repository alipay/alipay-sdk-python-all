#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneTypeListResult import SceneTypeListResult


class AlipayDigitalmgmtScenetypeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtScenetypeQueryResponse, self).__init__()
        self._scene_type_list_result = None

    @property
    def scene_type_list_result(self):
        return self._scene_type_list_result

    @scene_type_list_result.setter
    def scene_type_list_result(self, value):
        if isinstance(value, SceneTypeListResult):
            self._scene_type_list_result = value
        else:
            self._scene_type_list_result = SceneTypeListResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtScenetypeQueryResponse, self).parse_response_content(response_content)
        if 'scene_type_list_result' in response:
            self.scene_type_list_result = response['scene_type_list_result']
