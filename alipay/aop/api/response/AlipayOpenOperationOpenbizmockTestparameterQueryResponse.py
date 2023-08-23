#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenidComplex import OpenidComplex


class AlipayOpenOperationOpenbizmockTestparameterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationOpenbizmockTestparameterQueryResponse, self).__init__()
        self._result = None
        self._result_appidoutone = None
        self._result_appidouttwo = None
        self._result_oneuid = None
        self._result_oneuid_openid = None
        self._result_oneuid_oriiginal = None
        self._result_oneuid_oriiginal_openid = None
        self._result_test_original = None
        self._result_test_original_openid = None
        self._result_test_original_states = None
        self._result_test_original_states_openid = None
        self._result_test_original_states_test = None
        self._result_twouid = None
        self._result_twouid_openid = None
        self._result_twouid_oriiginal = None
        self._result_twouid_oriiginal_openid = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_appidoutone(self):
        return self._result_appidoutone

    @result_appidoutone.setter
    def result_appidoutone(self, value):
        self._result_appidoutone = value
    @property
    def result_appidouttwo(self):
        return self._result_appidouttwo

    @result_appidouttwo.setter
    def result_appidouttwo(self, value):
        self._result_appidouttwo = value
    @property
    def result_oneuid(self):
        return self._result_oneuid

    @result_oneuid.setter
    def result_oneuid(self, value):
        self._result_oneuid = value
    @property
    def result_oneuid_openid(self):
        return self._result_oneuid_openid

    @result_oneuid_openid.setter
    def result_oneuid_openid(self, value):
        self._result_oneuid_openid = value
    @property
    def result_oneuid_oriiginal(self):
        return self._result_oneuid_oriiginal

    @result_oneuid_oriiginal.setter
    def result_oneuid_oriiginal(self, value):
        self._result_oneuid_oriiginal = value
    @property
    def result_oneuid_oriiginal_openid(self):
        return self._result_oneuid_oriiginal_openid

    @result_oneuid_oriiginal_openid.setter
    def result_oneuid_oriiginal_openid(self, value):
        self._result_oneuid_oriiginal_openid = value
    @property
    def result_test_original(self):
        return self._result_test_original

    @result_test_original.setter
    def result_test_original(self, value):
        self._result_test_original = value
    @property
    def result_test_original_openid(self):
        return self._result_test_original_openid

    @result_test_original_openid.setter
    def result_test_original_openid(self, value):
        self._result_test_original_openid = value
    @property
    def result_test_original_states(self):
        return self._result_test_original_states

    @result_test_original_states.setter
    def result_test_original_states(self, value):
        self._result_test_original_states = value
    @property
    def result_test_original_states_openid(self):
        return self._result_test_original_states_openid

    @result_test_original_states_openid.setter
    def result_test_original_states_openid(self, value):
        self._result_test_original_states_openid = value
    @property
    def result_test_original_states_test(self):
        return self._result_test_original_states_test

    @result_test_original_states_test.setter
    def result_test_original_states_test(self, value):
        if isinstance(value, OpenidComplex):
            self._result_test_original_states_test = value
        else:
            self._result_test_original_states_test = OpenidComplex.from_alipay_dict(value)
    @property
    def result_twouid(self):
        return self._result_twouid

    @result_twouid.setter
    def result_twouid(self, value):
        self._result_twouid = value
    @property
    def result_twouid_openid(self):
        return self._result_twouid_openid

    @result_twouid_openid.setter
    def result_twouid_openid(self, value):
        self._result_twouid_openid = value
    @property
    def result_twouid_oriiginal(self):
        return self._result_twouid_oriiginal

    @result_twouid_oriiginal.setter
    def result_twouid_oriiginal(self, value):
        self._result_twouid_oriiginal = value
    @property
    def result_twouid_oriiginal_openid(self):
        return self._result_twouid_oriiginal_openid

    @result_twouid_oriiginal_openid.setter
    def result_twouid_oriiginal_openid(self, value):
        self._result_twouid_oriiginal_openid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationOpenbizmockTestparameterQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'result_appidoutone' in response:
            self.result_appidoutone = response['result_appidoutone']
        if 'result_appidouttwo' in response:
            self.result_appidouttwo = response['result_appidouttwo']
        if 'result_oneuid' in response:
            self.result_oneuid = response['result_oneuid']
        if 'result_oneuid_openid' in response:
            self.result_oneuid_openid = response['result_oneuid_openid']
        if 'result_oneuid_oriiginal' in response:
            self.result_oneuid_oriiginal = response['result_oneuid_oriiginal']
        if 'result_oneuid_oriiginal_openid' in response:
            self.result_oneuid_oriiginal_openid = response['result_oneuid_oriiginal_openid']
        if 'result_test_original' in response:
            self.result_test_original = response['result_test_original']
        if 'result_test_original_openid' in response:
            self.result_test_original_openid = response['result_test_original_openid']
        if 'result_test_original_states' in response:
            self.result_test_original_states = response['result_test_original_states']
        if 'result_test_original_states_openid' in response:
            self.result_test_original_states_openid = response['result_test_original_states_openid']
        if 'result_test_original_states_test' in response:
            self.result_test_original_states_test = response['result_test_original_states_test']
        if 'result_twouid' in response:
            self.result_twouid = response['result_twouid']
        if 'result_twouid_openid' in response:
            self.result_twouid_openid = response['result_twouid_openid']
        if 'result_twouid_oriiginal' in response:
            self.result_twouid_oriiginal = response['result_twouid_oriiginal']
        if 'result_twouid_oriiginal_openid' in response:
            self.result_twouid_oriiginal_openid = response['result_twouid_oriiginal_openid']
