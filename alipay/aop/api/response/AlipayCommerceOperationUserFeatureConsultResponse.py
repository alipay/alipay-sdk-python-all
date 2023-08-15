#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationUserFeatureConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationUserFeatureConsultResponse, self).__init__()
        self._biz_scene = None
        self._result = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationUserFeatureConsultResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'result' in response:
            self.result = response['result']
