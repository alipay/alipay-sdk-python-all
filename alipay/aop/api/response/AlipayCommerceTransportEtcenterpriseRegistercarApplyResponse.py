#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FailCarInfos import FailCarInfos


class AlipayCommerceTransportEtcenterpriseRegistercarApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseRegistercarApplyResponse, self).__init__()
        self._car_infos = None

    @property
    def car_infos(self):
        return self._car_infos

    @car_infos.setter
    def car_infos(self, value):
        if isinstance(value, FailCarInfos):
            self._car_infos = value
        else:
            self._car_infos = FailCarInfos.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseRegistercarApplyResponse, self).parse_response_content(response_content)
        if 'car_infos' in response:
            self.car_infos = response['car_infos']
