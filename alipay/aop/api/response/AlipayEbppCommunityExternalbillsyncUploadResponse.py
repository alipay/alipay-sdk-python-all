#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FailExternalSync import FailExternalSync


class AlipayEbppCommunityExternalbillsyncUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityExternalbillsyncUploadResponse, self).__init__()
        self._fail_count = None
        self._fail_external_sync = None
        self._success_count = None

    @property
    def fail_count(self):
        return self._fail_count

    @fail_count.setter
    def fail_count(self, value):
        self._fail_count = value
    @property
    def fail_external_sync(self):
        return self._fail_external_sync

    @fail_external_sync.setter
    def fail_external_sync(self, value):
        if isinstance(value, list):
            self._fail_external_sync = list()
            for i in value:
                if isinstance(i, FailExternalSync):
                    self._fail_external_sync.append(i)
                else:
                    self._fail_external_sync.append(FailExternalSync.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityExternalbillsyncUploadResponse, self).parse_response_content(response_content)
        if 'fail_count' in response:
            self.fail_count = response['fail_count']
        if 'fail_external_sync' in response:
            self.fail_external_sync = response['fail_external_sync']
        if 'success_count' in response:
            self.success_count = response['success_count']
