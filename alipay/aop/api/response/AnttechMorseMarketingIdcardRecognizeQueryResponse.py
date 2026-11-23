#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingIdcardRecognizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingIdcardRecognizeQueryResponse, self).__init__()
        self._biz_no = None
        self._check_result = None
        self._crop_status = None
        self._ocr_result = None
        self._ocr_status = None
        self._passed = None
        self._request_id = None
        self._side = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value
    @property
    def crop_status(self):
        return self._crop_status

    @crop_status.setter
    def crop_status(self, value):
        self._crop_status = value
    @property
    def ocr_result(self):
        return self._ocr_result

    @ocr_result.setter
    def ocr_result(self, value):
        self._ocr_result = value
    @property
    def ocr_status(self):
        return self._ocr_status

    @ocr_status.setter
    def ocr_status(self, value):
        self._ocr_status = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingIdcardRecognizeQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'check_result' in response:
            self.check_result = response['check_result']
        if 'crop_status' in response:
            self.crop_status = response['crop_status']
        if 'ocr_result' in response:
            self.ocr_result = response['ocr_result']
        if 'ocr_status' in response:
            self.ocr_status = response['ocr_status']
        if 'passed' in response:
            self.passed = response['passed']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'side' in response:
            self.side = response['side']
