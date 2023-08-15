#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CacheRule import CacheRule


class AlipayCloudCloudrunObjectstorageCacheruleBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageCacheruleBatchqueryResponse, self).__init__()
        self._cacherule_list = None

    @property
    def cacherule_list(self):
        return self._cacherule_list

    @cacherule_list.setter
    def cacherule_list(self, value):
        if isinstance(value, list):
            self._cacherule_list = list()
            for i in value:
                if isinstance(i, CacheRule):
                    self._cacherule_list.append(i)
                else:
                    self._cacherule_list.append(CacheRule.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageCacheruleBatchqueryResponse, self).parse_response_content(response_content)
        if 'cacherule_list' in response:
            self.cacherule_list = response['cacherule_list']
