#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbAdvertMissionQueryResponse import KbAdvertMissionQueryResponse
from alipay.aop.api.domain.KbAdvertProcessMissionResponse import KbAdvertProcessMissionResponse


class KoubeiAdvertCommissionMissionQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertCommissionMissionQueryResponse, self).__init__()
        self._data = None
        self._processing_data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, KbAdvertMissionQueryResponse):
                    self._data.append(i)
                else:
                    self._data.append(KbAdvertMissionQueryResponse.from_alipay_dict(i))
    @property
    def processing_data(self):
        return self._processing_data

    @processing_data.setter
    def processing_data(self, value):
        if isinstance(value, KbAdvertProcessMissionResponse):
            self._processing_data = value
        else:
            self._processing_data = KbAdvertProcessMissionResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertCommissionMissionQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'processing_data' in response:
            self.processing_data = response['processing_data']
