#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RegionState import RegionState


class AlipayMsaasMediarecogMmtcaftscvMachinegoodsAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmtcaftscvMachinegoodsAddResponse, self).__init__()
        self._regions = None

    @property
    def regions(self):
        return self._regions

    @regions.setter
    def regions(self, value):
        if isinstance(value, list):
            self._regions = list()
            for i in value:
                if isinstance(i, RegionState):
                    self._regions.append(i)
                else:
                    self._regions.append(RegionState.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogMmtcaftscvMachinegoodsAddResponse, self).parse_response_content(response_content)
        if 'regions' in response:
            self.regions = response['regions']
