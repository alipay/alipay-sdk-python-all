#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserDetail import UserDetail


class AlipayOpenOperationOpenbizmockOpenidtestingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationOpenbizmockOpenidtestingQueryResponse, self).__init__()
        self._result_extra_json = None
        self._result_extra_json_one = None
        self._result_extra_json_one_original = None
        self._result_extra_json_original = None
        self._result_test = None
        self._result_test_json = None
        self._result_test_json_original = None
        self._result_test_original = None
        self._result_test_wrong = None
        self._result_test_wrong_original = None
        self._result_user_detail = None
        self._result_user_detail_original = None
        self._result_user_id = None
        self._result_user_id_openid = None
        self._result_user_id_original = None

    @property
    def result_extra_json(self):
        return self._result_extra_json

    @result_extra_json.setter
    def result_extra_json(self, value):
        self._result_extra_json = value
    @property
    def result_extra_json_one(self):
        return self._result_extra_json_one

    @result_extra_json_one.setter
    def result_extra_json_one(self, value):
        self._result_extra_json_one = value
    @property
    def result_extra_json_one_original(self):
        return self._result_extra_json_one_original

    @result_extra_json_one_original.setter
    def result_extra_json_one_original(self, value):
        self._result_extra_json_one_original = value
    @property
    def result_extra_json_original(self):
        return self._result_extra_json_original

    @result_extra_json_original.setter
    def result_extra_json_original(self, value):
        self._result_extra_json_original = value
    @property
    def result_test(self):
        return self._result_test

    @result_test.setter
    def result_test(self, value):
        self._result_test = value
    @property
    def result_test_json(self):
        return self._result_test_json

    @result_test_json.setter
    def result_test_json(self, value):
        self._result_test_json = value
    @property
    def result_test_json_original(self):
        return self._result_test_json_original

    @result_test_json_original.setter
    def result_test_json_original(self, value):
        self._result_test_json_original = value
    @property
    def result_test_original(self):
        return self._result_test_original

    @result_test_original.setter
    def result_test_original(self, value):
        self._result_test_original = value
    @property
    def result_test_wrong(self):
        return self._result_test_wrong

    @result_test_wrong.setter
    def result_test_wrong(self, value):
        self._result_test_wrong = value
    @property
    def result_test_wrong_original(self):
        return self._result_test_wrong_original

    @result_test_wrong_original.setter
    def result_test_wrong_original(self, value):
        self._result_test_wrong_original = value
    @property
    def result_user_detail(self):
        return self._result_user_detail

    @result_user_detail.setter
    def result_user_detail(self, value):
        if isinstance(value, UserDetail):
            self._result_user_detail = value
        else:
            self._result_user_detail = UserDetail.from_alipay_dict(value)
    @property
    def result_user_detail_original(self):
        return self._result_user_detail_original

    @result_user_detail_original.setter
    def result_user_detail_original(self, value):
        self._result_user_detail_original = value
    @property
    def result_user_id(self):
        return self._result_user_id

    @result_user_id.setter
    def result_user_id(self, value):
        self._result_user_id = value
    @property
    def result_user_id_openid(self):
        return self._result_user_id_openid

    @result_user_id_openid.setter
    def result_user_id_openid(self, value):
        self._result_user_id_openid = value
    @property
    def result_user_id_original(self):
        return self._result_user_id_original

    @result_user_id_original.setter
    def result_user_id_original(self, value):
        self._result_user_id_original = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationOpenbizmockOpenidtestingQueryResponse, self).parse_response_content(response_content)
        if 'result_extra_json' in response:
            self.result_extra_json = response['result_extra_json']
        if 'result_extra_json_one' in response:
            self.result_extra_json_one = response['result_extra_json_one']
        if 'result_extra_json_one_original' in response:
            self.result_extra_json_one_original = response['result_extra_json_one_original']
        if 'result_extra_json_original' in response:
            self.result_extra_json_original = response['result_extra_json_original']
        if 'result_test' in response:
            self.result_test = response['result_test']
        if 'result_test_json' in response:
            self.result_test_json = response['result_test_json']
        if 'result_test_json_original' in response:
            self.result_test_json_original = response['result_test_json_original']
        if 'result_test_original' in response:
            self.result_test_original = response['result_test_original']
        if 'result_test_wrong' in response:
            self.result_test_wrong = response['result_test_wrong']
        if 'result_test_wrong_original' in response:
            self.result_test_wrong_original = response['result_test_wrong_original']
        if 'result_user_detail' in response:
            self.result_user_detail = response['result_user_detail']
        if 'result_user_detail_original' in response:
            self.result_user_detail_original = response['result_user_detail_original']
        if 'result_user_id' in response:
            self.result_user_id = response['result_user_id']
        if 'result_user_id_openid' in response:
            self.result_user_id_openid = response['result_user_id_openid']
        if 'result_user_id_original' in response:
            self.result_user_id_original = response['result_user_id_original']
