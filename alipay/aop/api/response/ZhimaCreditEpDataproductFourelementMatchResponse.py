#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EntBasicInfo import EntBasicInfo


class ZhimaCreditEpDataproductFourelementMatchResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDataproductFourelementMatchResponse, self).__init__()
        self._basic_info = None
        self._credit_code = None
        self._ent_name = None
        self._fr_cert_no = None
        self._fr_name = None
        self._match_code = None
        self._match_result_columns = None
        self._reg_no = None

    @property
    def basic_info(self):
        return self._basic_info

    @basic_info.setter
    def basic_info(self, value):
        if isinstance(value, EntBasicInfo):
            self._basic_info = value
        else:
            self._basic_info = EntBasicInfo.from_alipay_dict(value)
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def fr_cert_no(self):
        return self._fr_cert_no

    @fr_cert_no.setter
    def fr_cert_no(self, value):
        self._fr_cert_no = value
    @property
    def fr_name(self):
        return self._fr_name

    @fr_name.setter
    def fr_name(self, value):
        self._fr_name = value
    @property
    def match_code(self):
        return self._match_code

    @match_code.setter
    def match_code(self, value):
        self._match_code = value
    @property
    def match_result_columns(self):
        return self._match_result_columns

    @match_result_columns.setter
    def match_result_columns(self, value):
        if isinstance(value, list):
            self._match_result_columns = list()
            for i in value:
                self._match_result_columns.append(i)
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDataproductFourelementMatchResponse, self).parse_response_content(response_content)
        if 'basic_info' in response:
            self.basic_info = response['basic_info']
        if 'credit_code' in response:
            self.credit_code = response['credit_code']
        if 'ent_name' in response:
            self.ent_name = response['ent_name']
        if 'fr_cert_no' in response:
            self.fr_cert_no = response['fr_cert_no']
        if 'fr_name' in response:
            self.fr_name = response['fr_name']
        if 'match_code' in response:
            self.match_code = response['match_code']
        if 'match_result_columns' in response:
            self.match_result_columns = response['match_result_columns']
        if 'reg_no' in response:
            self.reg_no = response['reg_no']
