#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenidComplex import OpenidComplex
from alipay.aop.api.domain.OpenidComplex import OpenidComplex
from alipay.aop.api.domain.UserDetail import UserDetail


class AlipayOpenOperationOpenbizmockOpenidtestingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationOpenbizmockOpenidtestingQueryResponse, self).__init__()
        self._appid_out_one = None
        self._appid_out_three = None
        self._appid_out_two = None
        self._result_appidoutone = None
        self._result_appidoutthree = None
        self._result_appidouttwo = None
        self._result_extra_json = None
        self._result_extra_json_one = None
        self._result_extra_json_one_original = None
        self._result_extra_json_original = None
        self._result_one_open_id = None
        self._result_one_uid = None
        self._result_oneuid = None
        self._result_oneuid_open_id = None
        self._result_oneuid_original = None
        self._result_oneuid_original_open_id = None
        self._result_test = None
        self._result_test_json = None
        self._result_test_json_original = None
        self._result_test_openid = None
        self._result_test_original = None
        self._result_test_original_states = None
        self._result_test_test = None
        self._result_test_wrong = None
        self._result_test_wrong_original = None
        self._result_three_open_id = None
        self._result_three_uid = None
        self._result_threeuid = None
        self._result_threeuid_open_id = None
        self._result_threeuid_original = None
        self._result_threeuid_original_open_id = None
        self._result_two_open_id = None
        self._result_two_uid = None
        self._result_twouid = None
        self._result_twouid_open_id = None
        self._result_twouid_original = None
        self._result_twouid_original_open_id = None
        self._result_uid_list = None
        self._result_uid_list_open_id = None
        self._result_user_detail = None
        self._result_user_detail_original = None
        self._result_user_id = None
        self._result_user_id_openid = None
        self._result_user_id_original = None
        self._resulttwouid = None

    @property
    def appid_out_one(self):
        return self._appid_out_one

    @appid_out_one.setter
    def appid_out_one(self, value):
        self._appid_out_one = value
    @property
    def appid_out_three(self):
        return self._appid_out_three

    @appid_out_three.setter
    def appid_out_three(self, value):
        self._appid_out_three = value
    @property
    def appid_out_two(self):
        return self._appid_out_two

    @appid_out_two.setter
    def appid_out_two(self, value):
        self._appid_out_two = value
    @property
    def result_appidoutone(self):
        return self._result_appidoutone

    @result_appidoutone.setter
    def result_appidoutone(self, value):
        self._result_appidoutone = value
    @property
    def result_appidoutthree(self):
        return self._result_appidoutthree

    @result_appidoutthree.setter
    def result_appidoutthree(self, value):
        self._result_appidoutthree = value
    @property
    def result_appidouttwo(self):
        return self._result_appidouttwo

    @result_appidouttwo.setter
    def result_appidouttwo(self, value):
        self._result_appidouttwo = value
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
    def result_one_open_id(self):
        return self._result_one_open_id

    @result_one_open_id.setter
    def result_one_open_id(self, value):
        self._result_one_open_id = value
    @property
    def result_one_uid(self):
        return self._result_one_uid

    @result_one_uid.setter
    def result_one_uid(self, value):
        self._result_one_uid = value
    @property
    def result_oneuid(self):
        return self._result_oneuid

    @result_oneuid.setter
    def result_oneuid(self, value):
        self._result_oneuid = value
    @property
    def result_oneuid_open_id(self):
        return self._result_oneuid_open_id

    @result_oneuid_open_id.setter
    def result_oneuid_open_id(self, value):
        self._result_oneuid_open_id = value
    @property
    def result_oneuid_original(self):
        return self._result_oneuid_original

    @result_oneuid_original.setter
    def result_oneuid_original(self, value):
        self._result_oneuid_original = value
    @property
    def result_oneuid_original_open_id(self):
        return self._result_oneuid_original_open_id

    @result_oneuid_original_open_id.setter
    def result_oneuid_original_open_id(self, value):
        self._result_oneuid_original_open_id = value
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
    def result_test_openid(self):
        return self._result_test_openid

    @result_test_openid.setter
    def result_test_openid(self, value):
        self._result_test_openid = value
    @property
    def result_test_original(self):
        return self._result_test_original

    @result_test_original.setter
    def result_test_original(self, value):
        self._result_test_original = value
    @property
    def result_test_original_states(self):
        return self._result_test_original_states

    @result_test_original_states.setter
    def result_test_original_states(self, value):
        if isinstance(value, OpenidComplex):
            self._result_test_original_states = value
        else:
            self._result_test_original_states = OpenidComplex.from_alipay_dict(value)
    @property
    def result_test_test(self):
        return self._result_test_test

    @result_test_test.setter
    def result_test_test(self, value):
        if isinstance(value, OpenidComplex):
            self._result_test_test = value
        else:
            self._result_test_test = OpenidComplex.from_alipay_dict(value)
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
    def result_three_open_id(self):
        return self._result_three_open_id

    @result_three_open_id.setter
    def result_three_open_id(self, value):
        self._result_three_open_id = value
    @property
    def result_three_uid(self):
        return self._result_three_uid

    @result_three_uid.setter
    def result_three_uid(self, value):
        self._result_three_uid = value
    @property
    def result_threeuid(self):
        return self._result_threeuid

    @result_threeuid.setter
    def result_threeuid(self, value):
        self._result_threeuid = value
    @property
    def result_threeuid_open_id(self):
        return self._result_threeuid_open_id

    @result_threeuid_open_id.setter
    def result_threeuid_open_id(self, value):
        self._result_threeuid_open_id = value
    @property
    def result_threeuid_original(self):
        return self._result_threeuid_original

    @result_threeuid_original.setter
    def result_threeuid_original(self, value):
        self._result_threeuid_original = value
    @property
    def result_threeuid_original_open_id(self):
        return self._result_threeuid_original_open_id

    @result_threeuid_original_open_id.setter
    def result_threeuid_original_open_id(self, value):
        self._result_threeuid_original_open_id = value
    @property
    def result_two_open_id(self):
        return self._result_two_open_id

    @result_two_open_id.setter
    def result_two_open_id(self, value):
        self._result_two_open_id = value
    @property
    def result_two_uid(self):
        return self._result_two_uid

    @result_two_uid.setter
    def result_two_uid(self, value):
        self._result_two_uid = value
    @property
    def result_twouid(self):
        return self._result_twouid

    @result_twouid.setter
    def result_twouid(self, value):
        self._result_twouid = value
    @property
    def result_twouid_open_id(self):
        return self._result_twouid_open_id

    @result_twouid_open_id.setter
    def result_twouid_open_id(self, value):
        self._result_twouid_open_id = value
    @property
    def result_twouid_original(self):
        return self._result_twouid_original

    @result_twouid_original.setter
    def result_twouid_original(self, value):
        self._result_twouid_original = value
    @property
    def result_twouid_original_open_id(self):
        return self._result_twouid_original_open_id

    @result_twouid_original_open_id.setter
    def result_twouid_original_open_id(self, value):
        self._result_twouid_original_open_id = value
    @property
    def result_uid_list(self):
        return self._result_uid_list

    @result_uid_list.setter
    def result_uid_list(self, value):
        self._result_uid_list = value
    @property
    def result_uid_list_open_id(self):
        return self._result_uid_list_open_id

    @result_uid_list_open_id.setter
    def result_uid_list_open_id(self, value):
        self._result_uid_list_open_id = value
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
    @property
    def resulttwouid(self):
        return self._resulttwouid

    @resulttwouid.setter
    def resulttwouid(self, value):
        self._resulttwouid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationOpenbizmockOpenidtestingQueryResponse, self).parse_response_content(response_content)
        if 'appid_out_one' in response:
            self.appid_out_one = response['appid_out_one']
        if 'appid_out_three' in response:
            self.appid_out_three = response['appid_out_three']
        if 'appid_out_two' in response:
            self.appid_out_two = response['appid_out_two']
        if 'result_appidoutone' in response:
            self.result_appidoutone = response['result_appidoutone']
        if 'result_appidoutthree' in response:
            self.result_appidoutthree = response['result_appidoutthree']
        if 'result_appidouttwo' in response:
            self.result_appidouttwo = response['result_appidouttwo']
        if 'result_extra_json' in response:
            self.result_extra_json = response['result_extra_json']
        if 'result_extra_json_one' in response:
            self.result_extra_json_one = response['result_extra_json_one']
        if 'result_extra_json_one_original' in response:
            self.result_extra_json_one_original = response['result_extra_json_one_original']
        if 'result_extra_json_original' in response:
            self.result_extra_json_original = response['result_extra_json_original']
        if 'result_one_open_id' in response:
            self.result_one_open_id = response['result_one_open_id']
        if 'result_one_uid' in response:
            self.result_one_uid = response['result_one_uid']
        if 'result_oneuid' in response:
            self.result_oneuid = response['result_oneuid']
        if 'result_oneuid_open_id' in response:
            self.result_oneuid_open_id = response['result_oneuid_open_id']
        if 'result_oneuid_original' in response:
            self.result_oneuid_original = response['result_oneuid_original']
        if 'result_oneuid_original_open_id' in response:
            self.result_oneuid_original_open_id = response['result_oneuid_original_open_id']
        if 'result_test' in response:
            self.result_test = response['result_test']
        if 'result_test_json' in response:
            self.result_test_json = response['result_test_json']
        if 'result_test_json_original' in response:
            self.result_test_json_original = response['result_test_json_original']
        if 'result_test_openid' in response:
            self.result_test_openid = response['result_test_openid']
        if 'result_test_original' in response:
            self.result_test_original = response['result_test_original']
        if 'result_test_original_states' in response:
            self.result_test_original_states = response['result_test_original_states']
        if 'result_test_test' in response:
            self.result_test_test = response['result_test_test']
        if 'result_test_wrong' in response:
            self.result_test_wrong = response['result_test_wrong']
        if 'result_test_wrong_original' in response:
            self.result_test_wrong_original = response['result_test_wrong_original']
        if 'result_three_open_id' in response:
            self.result_three_open_id = response['result_three_open_id']
        if 'result_three_uid' in response:
            self.result_three_uid = response['result_three_uid']
        if 'result_threeuid' in response:
            self.result_threeuid = response['result_threeuid']
        if 'result_threeuid_open_id' in response:
            self.result_threeuid_open_id = response['result_threeuid_open_id']
        if 'result_threeuid_original' in response:
            self.result_threeuid_original = response['result_threeuid_original']
        if 'result_threeuid_original_open_id' in response:
            self.result_threeuid_original_open_id = response['result_threeuid_original_open_id']
        if 'result_two_open_id' in response:
            self.result_two_open_id = response['result_two_open_id']
        if 'result_two_uid' in response:
            self.result_two_uid = response['result_two_uid']
        if 'result_twouid' in response:
            self.result_twouid = response['result_twouid']
        if 'result_twouid_open_id' in response:
            self.result_twouid_open_id = response['result_twouid_open_id']
        if 'result_twouid_original' in response:
            self.result_twouid_original = response['result_twouid_original']
        if 'result_twouid_original_open_id' in response:
            self.result_twouid_original_open_id = response['result_twouid_original_open_id']
        if 'result_uid_list' in response:
            self.result_uid_list = response['result_uid_list']
        if 'result_uid_list_open_id' in response:
            self.result_uid_list_open_id = response['result_uid_list_open_id']
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
        if 'resulttwouid' in response:
            self.resulttwouid = response['resulttwouid']
