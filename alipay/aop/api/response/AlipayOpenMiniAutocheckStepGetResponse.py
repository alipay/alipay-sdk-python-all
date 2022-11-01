#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SlmServiceAtomicInfoVO import SlmServiceAtomicInfoVO


class AlipayOpenMiniAutocheckStepGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAutocheckStepGetResponse, self).__init__()
        self._slm_service_atomic_info = None

    @property
    def slm_service_atomic_info(self):
        return self._slm_service_atomic_info

    @slm_service_atomic_info.setter
    def slm_service_atomic_info(self, value):
        if isinstance(value, list):
            self._slm_service_atomic_info = list()
            for i in value:
                if isinstance(i, SlmServiceAtomicInfoVO):
                    self._slm_service_atomic_info.append(i)
                else:
                    self._slm_service_atomic_info.append(SlmServiceAtomicInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAutocheckStepGetResponse, self).parse_response_content(response_content)
        if 'slm_service_atomic_info' in response:
            self.slm_service_atomic_info = response['slm_service_atomic_info']
