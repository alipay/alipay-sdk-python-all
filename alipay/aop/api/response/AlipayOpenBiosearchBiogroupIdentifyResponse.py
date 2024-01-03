#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BioSearchApiResult import BioSearchApiResult


class AlipayOpenBiosearchBiogroupIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenBiosearchBiogroupIdentifyResponse, self).__init__()
        self._bio_results = None

    @property
    def bio_results(self):
        return self._bio_results

    @bio_results.setter
    def bio_results(self, value):
        if isinstance(value, list):
            self._bio_results = list()
            for i in value:
                if isinstance(i, BioSearchApiResult):
                    self._bio_results.append(i)
                else:
                    self._bio_results.append(BioSearchApiResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenBiosearchBiogroupIdentifyResponse, self).parse_response_content(response_content)
        if 'bio_results' in response:
            self.bio_results = response['bio_results']
