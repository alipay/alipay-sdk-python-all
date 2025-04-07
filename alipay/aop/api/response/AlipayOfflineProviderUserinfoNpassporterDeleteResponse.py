#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderUserinfoNpassporterDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderUserinfoNpassporterDeleteResponse, self).__init__()
        self._fail_out_biz_no = None
        self._success_out_biz_no = None

    @property
    def fail_out_biz_no(self):
        return self._fail_out_biz_no

    @fail_out_biz_no.setter
    def fail_out_biz_no(self, value):
        if isinstance(value, list):
            self._fail_out_biz_no = list()
            for i in value:
                self._fail_out_biz_no.append(i)
    @property
    def success_out_biz_no(self):
        return self._success_out_biz_no

    @success_out_biz_no.setter
    def success_out_biz_no(self, value):
        if isinstance(value, list):
            self._success_out_biz_no = list()
            for i in value:
                self._success_out_biz_no.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderUserinfoNpassporterDeleteResponse, self).parse_response_content(response_content)
        if 'fail_out_biz_no' in response:
            self.fail_out_biz_no = response['fail_out_biz_no']
        if 'success_out_biz_no' in response:
            self.success_out_biz_no = response['success_out_biz_no']
