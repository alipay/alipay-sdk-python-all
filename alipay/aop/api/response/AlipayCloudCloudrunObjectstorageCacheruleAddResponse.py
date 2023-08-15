#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CacheRule import CacheRule


class AlipayCloudCloudrunObjectstorageCacheruleAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageCacheruleAddResponse, self).__init__()
        self._cacherule = None

    @property
    def cacherule(self):
        return self._cacherule

    @cacherule.setter
    def cacherule(self, value):
        if isinstance(value, CacheRule):
            self._cacherule = value
        else:
            self._cacherule = CacheRule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageCacheruleAddResponse, self).parse_response_content(response_content)
        if 'cacherule' in response:
            self.cacherule = response['cacherule']
