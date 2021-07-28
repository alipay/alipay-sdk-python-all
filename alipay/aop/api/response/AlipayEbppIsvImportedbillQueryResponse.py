#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIsvImportedbillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIsvImportedbillQueryResponse, self).__init__()
        self._analysis_fail_count = None
        self._analysis_suc_count = None
        self._import_fail_count = None
        self._import_suc_count = None
        self._total_count = None

    @property
    def analysis_fail_count(self):
        return self._analysis_fail_count

    @analysis_fail_count.setter
    def analysis_fail_count(self, value):
        self._analysis_fail_count = value
    @property
    def analysis_suc_count(self):
        return self._analysis_suc_count

    @analysis_suc_count.setter
    def analysis_suc_count(self, value):
        self._analysis_suc_count = value
    @property
    def import_fail_count(self):
        return self._import_fail_count

    @import_fail_count.setter
    def import_fail_count(self, value):
        self._import_fail_count = value
    @property
    def import_suc_count(self):
        return self._import_suc_count

    @import_suc_count.setter
    def import_suc_count(self, value):
        self._import_suc_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIsvImportedbillQueryResponse, self).parse_response_content(response_content)
        if 'analysis_fail_count' in response:
            self.analysis_fail_count = response['analysis_fail_count']
        if 'analysis_suc_count' in response:
            self.analysis_suc_count = response['analysis_suc_count']
        if 'import_fail_count' in response:
            self.import_fail_count = response['import_fail_count']
        if 'import_suc_count' in response:
            self.import_suc_count = response['import_suc_count']
        if 'total_count' in response:
            self.total_count = response['total_count']
