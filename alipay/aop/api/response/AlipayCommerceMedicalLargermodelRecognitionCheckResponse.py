#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalLargermodelRecognitionCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelRecognitionCheckResponse, self).__init__()
        self._afts_id = None
        self._classify_result = None
        self._compressed_pic_url = None
        self._pic_type = None
        self._query = None
        self._tips = None
        self._url = None
        self._verification_result = None

    @property
    def afts_id(self):
        return self._afts_id

    @afts_id.setter
    def afts_id(self, value):
        self._afts_id = value
    @property
    def classify_result(self):
        return self._classify_result

    @classify_result.setter
    def classify_result(self, value):
        self._classify_result = value
    @property
    def compressed_pic_url(self):
        return self._compressed_pic_url

    @compressed_pic_url.setter
    def compressed_pic_url(self, value):
        self._compressed_pic_url = value
    @property
    def pic_type(self):
        return self._pic_type

    @pic_type.setter
    def pic_type(self, value):
        self._pic_type = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def verification_result(self):
        return self._verification_result

    @verification_result.setter
    def verification_result(self, value):
        self._verification_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelRecognitionCheckResponse, self).parse_response_content(response_content)
        if 'afts_id' in response:
            self.afts_id = response['afts_id']
        if 'classify_result' in response:
            self.classify_result = response['classify_result']
        if 'compressed_pic_url' in response:
            self.compressed_pic_url = response['compressed_pic_url']
        if 'pic_type' in response:
            self.pic_type = response['pic_type']
        if 'query' in response:
            self.query = response['query']
        if 'tips' in response:
            self.tips = response['tips']
        if 'url' in response:
            self.url = response['url']
        if 'verification_result' in response:
            self.verification_result = response['verification_result']
