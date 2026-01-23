#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Qualification import Qualification


class AlipayMarketingQualificationConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingQualificationConsultResponse, self).__init__()
        self._qualifications = None

    @property
    def qualifications(self):
        return self._qualifications

    @qualifications.setter
    def qualifications(self, value):
        if isinstance(value, list):
            self._qualifications = list()
            for i in value:
                if isinstance(i, Qualification):
                    self._qualifications.append(i)
                else:
                    self._qualifications.append(Qualification.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingQualificationConsultResponse, self).parse_response_content(response_content)
        if 'qualifications' in response:
            self.qualifications = response['qualifications']
