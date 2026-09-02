#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdSeriesAppCompilationResp import AdSeriesAppCompilationResp


class AlipayDataDataserviceAdcampaignSeriesappcompilationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignSeriesappcompilationQueryResponse, self).__init__()
        self._compilation_list = None

    @property
    def compilation_list(self):
        return self._compilation_list

    @compilation_list.setter
    def compilation_list(self, value):
        if isinstance(value, list):
            self._compilation_list = list()
            for i in value:
                if isinstance(i, AdSeriesAppCompilationResp):
                    self._compilation_list.append(i)
                else:
                    self._compilation_list.append(AdSeriesAppCompilationResp.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignSeriesappcompilationQueryResponse, self).parse_response_content(response_content)
        if 'compilation_list' in response:
            self.compilation_list = response['compilation_list']
