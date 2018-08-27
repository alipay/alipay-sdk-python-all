#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataFindataOperatorUserinfoCertifyResponse(AlipayResponse):

    def __init__(self):
        super(SsdataFindataOperatorUserinfoCertifyResponse, self).__init__()
        self._biz_no = None
        self._form_list = None
        self._org_biz_no = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def form_list(self):
        return self._form_list

    @form_list.setter
    def form_list(self, value):
        if isinstance(value, list):
            self._form_list = list()
            for i in value:
                self._form_list.append(i)
    @property
    def org_biz_no(self):
        return self._org_biz_no

    @org_biz_no.setter
    def org_biz_no(self, value):
        self._org_biz_no = value

    def parse_response_content(self, response_content):
        response = super(SsdataFindataOperatorUserinfoCertifyResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'form_list' in response:
            self.form_list = response['form_list']
        if 'org_biz_no' in response:
            self.org_biz_no = response['org_biz_no']
