#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CostDistributionOcrResultNode import CostDistributionOcrResultNode


class AlipaySocialBaseLifecreationShortplayCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseLifecreationShortplayCreateResponse, self).__init__()
        self._album_id = None
        self._cost_distribution_ocr_result = None
        self._lib_version = None

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
    @property
    def cost_distribution_ocr_result(self):
        return self._cost_distribution_ocr_result

    @cost_distribution_ocr_result.setter
    def cost_distribution_ocr_result(self, value):
        if isinstance(value, CostDistributionOcrResultNode):
            self._cost_distribution_ocr_result = value
        else:
            self._cost_distribution_ocr_result = CostDistributionOcrResultNode.from_alipay_dict(value)
    @property
    def lib_version(self):
        return self._lib_version

    @lib_version.setter
    def lib_version(self, value):
        self._lib_version = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseLifecreationShortplayCreateResponse, self).parse_response_content(response_content)
        if 'album_id' in response:
            self.album_id = response['album_id']
        if 'cost_distribution_ocr_result' in response:
            self.cost_distribution_ocr_result = response['cost_distribution_ocr_result']
        if 'lib_version' in response:
            self.lib_version = response['lib_version']
