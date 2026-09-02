#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeepFakeResult import DeepFakeResult
from alipay.aop.api.domain.DeepFakeResult import DeepFakeResult
from alipay.aop.api.domain.DeepFakeResult import DeepFakeResult
from alipay.aop.api.domain.DeepFakeResult import DeepFakeResult
from alipay.aop.api.domain.DeepFakeResult import DeepFakeResult


class DatadigitalFincloudGeneralsaasDeepfakeNewCheckResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasDeepfakeNewCheckResponse, self).__init__()
        self._certify_id = None
        self._colorprint_result = None
        self._exif_ps_result = None
        self._jieping_result = None
        self._paiping_result = None
        self._passed = None
        self._ps_result = None
        self._tamper_ps_result = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def colorprint_result(self):
        return self._colorprint_result

    @colorprint_result.setter
    def colorprint_result(self, value):
        if isinstance(value, DeepFakeResult):
            self._colorprint_result = value
        else:
            self._colorprint_result = DeepFakeResult.from_alipay_dict(value)
    @property
    def exif_ps_result(self):
        return self._exif_ps_result

    @exif_ps_result.setter
    def exif_ps_result(self, value):
        self._exif_ps_result = value
    @property
    def jieping_result(self):
        return self._jieping_result

    @jieping_result.setter
    def jieping_result(self, value):
        if isinstance(value, DeepFakeResult):
            self._jieping_result = value
        else:
            self._jieping_result = DeepFakeResult.from_alipay_dict(value)
    @property
    def paiping_result(self):
        return self._paiping_result

    @paiping_result.setter
    def paiping_result(self, value):
        if isinstance(value, DeepFakeResult):
            self._paiping_result = value
        else:
            self._paiping_result = DeepFakeResult.from_alipay_dict(value)
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value
    @property
    def ps_result(self):
        return self._ps_result

    @ps_result.setter
    def ps_result(self, value):
        if isinstance(value, DeepFakeResult):
            self._ps_result = value
        else:
            self._ps_result = DeepFakeResult.from_alipay_dict(value)
    @property
    def tamper_ps_result(self):
        return self._tamper_ps_result

    @tamper_ps_result.setter
    def tamper_ps_result(self, value):
        if isinstance(value, DeepFakeResult):
            self._tamper_ps_result = value
        else:
            self._tamper_ps_result = DeepFakeResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasDeepfakeNewCheckResponse, self).parse_response_content(response_content)
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'colorprint_result' in response:
            self.colorprint_result = response['colorprint_result']
        if 'exif_ps_result' in response:
            self.exif_ps_result = response['exif_ps_result']
        if 'jieping_result' in response:
            self.jieping_result = response['jieping_result']
        if 'paiping_result' in response:
            self.paiping_result = response['paiping_result']
        if 'passed' in response:
            self.passed = response['passed']
        if 'ps_result' in response:
            self.ps_result = response['ps_result']
        if 'tamper_ps_result' in response:
            self.tamper_ps_result = response['tamper_ps_result']
