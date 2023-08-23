#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PackageUsage import PackageUsage


class AlipayCloudCloudbaseResourceusagePackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourceusagePackageQueryResponse, self).__init__()
        self._end_time = None
        self._package_usages = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def package_usages(self):
        return self._package_usages

    @package_usages.setter
    def package_usages(self, value):
        if isinstance(value, list):
            self._package_usages = list()
            for i in value:
                if isinstance(i, PackageUsage):
                    self._package_usages.append(i)
                else:
                    self._package_usages.append(PackageUsage.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourceusagePackageQueryResponse, self).parse_response_content(response_content)
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'package_usages' in response:
            self.package_usages = response['package_usages']
        if 'start_time' in response:
            self.start_time = response['start_time']
