#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentCarSpuExpoInfo import RentCarSpuExpoInfo


class AlipayEcoMycarRentcarSpuexpoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarRentcarSpuexpoQueryResponse, self).__init__()
        self._expo_infos = None
        self._total_size = None

    @property
    def expo_infos(self):
        return self._expo_infos

    @expo_infos.setter
    def expo_infos(self, value):
        if isinstance(value, list):
            self._expo_infos = list()
            for i in value:
                if isinstance(i, RentCarSpuExpoInfo):
                    self._expo_infos.append(i)
                else:
                    self._expo_infos.append(RentCarSpuExpoInfo.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarRentcarSpuexpoQueryResponse, self).parse_response_content(response_content)
        if 'expo_infos' in response:
            self.expo_infos = response['expo_infos']
        if 'total_size' in response:
            self.total_size = response['total_size']
