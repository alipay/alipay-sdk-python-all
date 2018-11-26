#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PintuanUserInfos import PintuanUserInfos


class AlipayUserPortraitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPortraitQueryResponse, self).__init__()
        self._pintuan_user_infos = None

    @property
    def pintuan_user_infos(self):
        return self._pintuan_user_infos

    @pintuan_user_infos.setter
    def pintuan_user_infos(self, value):
        if isinstance(value, list):
            self._pintuan_user_infos = list()
            for i in value:
                if isinstance(i, PintuanUserInfos):
                    self._pintuan_user_infos.append(i)
                else:
                    self._pintuan_user_infos.append(PintuanUserInfos.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserPortraitQueryResponse, self).parse_response_content(response_content)
        if 'pintuan_user_infos' in response:
            self.pintuan_user_infos = response['pintuan_user_infos']
