#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogAivisionstoredAiretailriskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAivisionstoredAiretailriskQueryResponse, self).__init__()
        self._desc = None
        self._has_risk = None
        self._pics = None
        self._report_time = None
        self._risk_type = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def has_risk(self):
        return self._has_risk

    @has_risk.setter
    def has_risk(self, value):
        self._has_risk = value
    @property
    def pics(self):
        return self._pics

    @pics.setter
    def pics(self, value):
        if isinstance(value, list):
            self._pics = list()
            for i in value:
                self._pics.append(i)
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAivisionstoredAiretailriskQueryResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
        if 'has_risk' in response:
            self.has_risk = response['has_risk']
        if 'pics' in response:
            self.pics = response['pics']
        if 'report_time' in response:
            self.report_time = response['report_time']
        if 'risk_type' in response:
            self.risk_type = response['risk_type']
