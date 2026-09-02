#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasDeepfakeDetectResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasDeepfakeDetectResponse, self).__init__()
        self._certify_id = None
        self._colorprint_result = None
        self._duplicate_upload_result = None
        self._jieping_result = None
        self._paiping_result = None
        self._passed = None
        self._ps_result = None
        self._same_background_result = None
        self._same_face_result = None
        self._same_signature_result = None
        self._tamper_ps_result = None
        self._watermark_result = None

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
        self._colorprint_result = value
    @property
    def duplicate_upload_result(self):
        return self._duplicate_upload_result

    @duplicate_upload_result.setter
    def duplicate_upload_result(self, value):
        self._duplicate_upload_result = value
    @property
    def jieping_result(self):
        return self._jieping_result

    @jieping_result.setter
    def jieping_result(self, value):
        self._jieping_result = value
    @property
    def paiping_result(self):
        return self._paiping_result

    @paiping_result.setter
    def paiping_result(self, value):
        self._paiping_result = value
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
        self._ps_result = value
    @property
    def same_background_result(self):
        return self._same_background_result

    @same_background_result.setter
    def same_background_result(self, value):
        self._same_background_result = value
    @property
    def same_face_result(self):
        return self._same_face_result

    @same_face_result.setter
    def same_face_result(self, value):
        self._same_face_result = value
    @property
    def same_signature_result(self):
        return self._same_signature_result

    @same_signature_result.setter
    def same_signature_result(self, value):
        self._same_signature_result = value
    @property
    def tamper_ps_result(self):
        return self._tamper_ps_result

    @tamper_ps_result.setter
    def tamper_ps_result(self, value):
        self._tamper_ps_result = value
    @property
    def watermark_result(self):
        return self._watermark_result

    @watermark_result.setter
    def watermark_result(self, value):
        self._watermark_result = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasDeepfakeDetectResponse, self).parse_response_content(response_content)
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'colorprint_result' in response:
            self.colorprint_result = response['colorprint_result']
        if 'duplicate_upload_result' in response:
            self.duplicate_upload_result = response['duplicate_upload_result']
        if 'jieping_result' in response:
            self.jieping_result = response['jieping_result']
        if 'paiping_result' in response:
            self.paiping_result = response['paiping_result']
        if 'passed' in response:
            self.passed = response['passed']
        if 'ps_result' in response:
            self.ps_result = response['ps_result']
        if 'same_background_result' in response:
            self.same_background_result = response['same_background_result']
        if 'same_face_result' in response:
            self.same_face_result = response['same_face_result']
        if 'same_signature_result' in response:
            self.same_signature_result = response['same_signature_result']
        if 'tamper_ps_result' in response:
            self.tamper_ps_result = response['tamper_ps_result']
        if 'watermark_result' in response:
            self.watermark_result = response['watermark_result']
