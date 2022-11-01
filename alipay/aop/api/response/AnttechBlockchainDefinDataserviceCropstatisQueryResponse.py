#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CropsStatisticsInfo import CropsStatisticsInfo


class AnttechBlockchainDefinDataserviceCropstatisQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinDataserviceCropstatisQueryResponse, self).__init__()
        self._crop_statistics = None

    @property
    def crop_statistics(self):
        return self._crop_statistics

    @crop_statistics.setter
    def crop_statistics(self, value):
        if isinstance(value, list):
            self._crop_statistics = list()
            for i in value:
                if isinstance(i, CropsStatisticsInfo):
                    self._crop_statistics.append(i)
                else:
                    self._crop_statistics.append(CropsStatisticsInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinDataserviceCropstatisQueryResponse, self).parse_response_content(response_content)
        if 'crop_statistics' in response:
            self.crop_statistics = response['crop_statistics']
