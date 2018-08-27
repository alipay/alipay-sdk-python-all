#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StationDetailInfo import StationDetailInfo


class AlipayCommerceCityfacilitatorStationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorStationQueryResponse, self).__init__()
        self._support_starts = None

    @property
    def support_starts(self):
        return self._support_starts

    @support_starts.setter
    def support_starts(self, value):
        if isinstance(value, list):
            self._support_starts = list()
            for i in value:
                if isinstance(i, StationDetailInfo):
                    self._support_starts.append(i)
                else:
                    self._support_starts.append(StationDetailInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorStationQueryResponse, self).parse_response_content(response_content)
        if 'support_starts' in response:
            self.support_starts = response['support_starts']
