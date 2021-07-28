#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityCopyResult import ActivityCopyResult


class AntMerchantExpandIndirectActivityCopyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectActivityCopyResponse, self).__init__()
        self._copy_result = None

    @property
    def copy_result(self):
        return self._copy_result

    @copy_result.setter
    def copy_result(self, value):
        if isinstance(value, list):
            self._copy_result = list()
            for i in value:
                if isinstance(i, ActivityCopyResult):
                    self._copy_result.append(i)
                else:
                    self._copy_result.append(ActivityCopyResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectActivityCopyResponse, self).parse_response_content(response_content)
        if 'copy_result' in response:
            self.copy_result = response['copy_result']
