#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIotfmCheckbindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIotfmCheckbindQueryResponse, self).__init__()
        self._has_bind_fm = None

    @property
    def has_bind_fm(self):
        return self._has_bind_fm

    @has_bind_fm.setter
    def has_bind_fm(self, value):
        self._has_bind_fm = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIotfmCheckbindQueryResponse, self).parse_response_content(response_content)
        if 'has_bind_fm' in response:
            self.has_bind_fm = response['has_bind_fm']
