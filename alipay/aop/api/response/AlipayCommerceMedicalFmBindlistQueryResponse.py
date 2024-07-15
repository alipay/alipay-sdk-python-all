#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FmBindFmVO import FmBindFmVO


class AlipayCommerceMedicalFmBindlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalFmBindlistQueryResponse, self).__init__()
        self._bind_list = None

    @property
    def bind_list(self):
        return self._bind_list

    @bind_list.setter
    def bind_list(self, value):
        if isinstance(value, list):
            self._bind_list = list()
            for i in value:
                if isinstance(i, FmBindFmVO):
                    self._bind_list.append(i)
                else:
                    self._bind_list.append(FmBindFmVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalFmBindlistQueryResponse, self).parse_response_content(response_content)
        if 'bind_list' in response:
            self.bind_list = response['bind_list']
