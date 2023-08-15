#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenidComplex import OpenidComplex
from alipay.aop.api.domain.UserDetail import UserDetail


class AlipayOpenOperationOpenbizmockOpenidtestingQueryModel(object):

    def __init__(self):
        self._appid_one = None
        self._appid_out_one = None
        self._appid_out_three = None
        self._appid_out_two = None
        self._appid_three = None
        self._appid_two = None
        self._extra_json = None
        self._extra_json_1 = None
        self._lalala_openid = None
        self._lalala_real_open_id = None
        self._lalalala = None
        self._one_open_id = None
        self._one_uid = None
        self._open_id = None
        self._result_oneuid_original = None
        self._test = None
        self._test_json = None
        self._test_wrong = None
        self._three_open_id = None
        self._three_uid = None
        self._two_open_id = None
        self._two_uid = None
        self._uid_list = None
        self._uid_list_open_id_list = None
        self._user_detail = None
        self._user_id = None

    @property
    def appid_one(self):
        return self._appid_one

    @appid_one.setter
    def appid_one(self, value):
        self._appid_one = value
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
    def appid_three(self):
        return self._appid_three

    @appid_three.setter
    def appid_three(self, value):
        self._appid_three = value
    @property
    def appid_two(self):
        return self._appid_two

    @appid_two.setter
    def appid_two(self, value):
        self._appid_two = value
    @property
    def extra_json(self):
        return self._extra_json

    @extra_json.setter
    def extra_json(self, value):
        self._extra_json = value
    @property
    def extra_json_1(self):
        return self._extra_json_1

    @extra_json_1.setter
    def extra_json_1(self, value):
        self._extra_json_1 = value
    @property
    def lalala_openid(self):
        return self._lalala_openid

    @lalala_openid.setter
    def lalala_openid(self, value):
        self._lalala_openid = value
    @property
    def lalala_real_open_id(self):
        return self._lalala_real_open_id

    @lalala_real_open_id.setter
    def lalala_real_open_id(self, value):
        self._lalala_real_open_id = value
    @property
    def lalalala(self):
        return self._lalalala

    @lalalala.setter
    def lalalala(self, value):
        self._lalalala = value
    @property
    def one_open_id(self):
        return self._one_open_id

    @one_open_id.setter
    def one_open_id(self, value):
        self._one_open_id = value
    @property
    def one_uid(self):
        return self._one_uid

    @one_uid.setter
    def one_uid(self, value):
        self._one_uid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def result_oneuid_original(self):
        return self._result_oneuid_original

    @result_oneuid_original.setter
    def result_oneuid_original(self, value):
        self._result_oneuid_original = value
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, OpenidComplex):
            self._test = value
        else:
            self._test = OpenidComplex.from_alipay_dict(value)
    @property
    def test_json(self):
        return self._test_json

    @test_json.setter
    def test_json(self, value):
        self._test_json = value
    @property
    def test_wrong(self):
        return self._test_wrong

    @test_wrong.setter
    def test_wrong(self, value):
        self._test_wrong = value
    @property
    def three_open_id(self):
        return self._three_open_id

    @three_open_id.setter
    def three_open_id(self, value):
        self._three_open_id = value
    @property
    def three_uid(self):
        return self._three_uid

    @three_uid.setter
    def three_uid(self, value):
        self._three_uid = value
    @property
    def two_open_id(self):
        return self._two_open_id

    @two_open_id.setter
    def two_open_id(self, value):
        self._two_open_id = value
    @property
    def two_uid(self):
        return self._two_uid

    @two_uid.setter
    def two_uid(self, value):
        self._two_uid = value
    @property
    def uid_list(self):
        return self._uid_list

    @uid_list.setter
    def uid_list(self, value):
        if isinstance(value, list):
            self._uid_list = list()
            for i in value:
                self._uid_list.append(i)
    @property
    def uid_list_open_id_list(self):
        return self._uid_list_open_id_list

    @uid_list_open_id_list.setter
    def uid_list_open_id_list(self, value):
        if isinstance(value, list):
            self._uid_list_open_id_list = list()
            for i in value:
                self._uid_list_open_id_list.append(i)
    @property
    def user_detail(self):
        return self._user_detail

    @user_detail.setter
    def user_detail(self, value):
        if isinstance(value, UserDetail):
            self._user_detail = value
        else:
            self._user_detail = UserDetail.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.appid_one:
            if hasattr(self.appid_one, 'to_alipay_dict'):
                params['appid_one'] = self.appid_one.to_alipay_dict()
            else:
                params['appid_one'] = self.appid_one
        if self.appid_out_one:
            if hasattr(self.appid_out_one, 'to_alipay_dict'):
                params['appid_out_one'] = self.appid_out_one.to_alipay_dict()
            else:
                params['appid_out_one'] = self.appid_out_one
        if self.appid_out_three:
            if hasattr(self.appid_out_three, 'to_alipay_dict'):
                params['appid_out_three'] = self.appid_out_three.to_alipay_dict()
            else:
                params['appid_out_three'] = self.appid_out_three
        if self.appid_out_two:
            if hasattr(self.appid_out_two, 'to_alipay_dict'):
                params['appid_out_two'] = self.appid_out_two.to_alipay_dict()
            else:
                params['appid_out_two'] = self.appid_out_two
        if self.appid_three:
            if hasattr(self.appid_three, 'to_alipay_dict'):
                params['appid_three'] = self.appid_three.to_alipay_dict()
            else:
                params['appid_three'] = self.appid_three
        if self.appid_two:
            if hasattr(self.appid_two, 'to_alipay_dict'):
                params['appid_two'] = self.appid_two.to_alipay_dict()
            else:
                params['appid_two'] = self.appid_two
        if self.extra_json:
            if hasattr(self.extra_json, 'to_alipay_dict'):
                params['extra_json'] = self.extra_json.to_alipay_dict()
            else:
                params['extra_json'] = self.extra_json
        if self.extra_json_1:
            if hasattr(self.extra_json_1, 'to_alipay_dict'):
                params['extra_json_1'] = self.extra_json_1.to_alipay_dict()
            else:
                params['extra_json_1'] = self.extra_json_1
        if self.lalala_openid:
            if hasattr(self.lalala_openid, 'to_alipay_dict'):
                params['lalala_openid'] = self.lalala_openid.to_alipay_dict()
            else:
                params['lalala_openid'] = self.lalala_openid
        if self.lalala_real_open_id:
            if hasattr(self.lalala_real_open_id, 'to_alipay_dict'):
                params['lalala_real_open_id'] = self.lalala_real_open_id.to_alipay_dict()
            else:
                params['lalala_real_open_id'] = self.lalala_real_open_id
        if self.lalalala:
            if hasattr(self.lalalala, 'to_alipay_dict'):
                params['lalalala'] = self.lalalala.to_alipay_dict()
            else:
                params['lalalala'] = self.lalalala
        if self.one_open_id:
            if hasattr(self.one_open_id, 'to_alipay_dict'):
                params['one_open_id'] = self.one_open_id.to_alipay_dict()
            else:
                params['one_open_id'] = self.one_open_id
        if self.one_uid:
            if hasattr(self.one_uid, 'to_alipay_dict'):
                params['one_uid'] = self.one_uid.to_alipay_dict()
            else:
                params['one_uid'] = self.one_uid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.result_oneuid_original:
            if hasattr(self.result_oneuid_original, 'to_alipay_dict'):
                params['result_oneuid_original'] = self.result_oneuid_original.to_alipay_dict()
            else:
                params['result_oneuid_original'] = self.result_oneuid_original
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        if self.test_json:
            if hasattr(self.test_json, 'to_alipay_dict'):
                params['test_json'] = self.test_json.to_alipay_dict()
            else:
                params['test_json'] = self.test_json
        if self.test_wrong:
            if hasattr(self.test_wrong, 'to_alipay_dict'):
                params['test_wrong'] = self.test_wrong.to_alipay_dict()
            else:
                params['test_wrong'] = self.test_wrong
        if self.three_open_id:
            if hasattr(self.three_open_id, 'to_alipay_dict'):
                params['three_open_id'] = self.three_open_id.to_alipay_dict()
            else:
                params['three_open_id'] = self.three_open_id
        if self.three_uid:
            if hasattr(self.three_uid, 'to_alipay_dict'):
                params['three_uid'] = self.three_uid.to_alipay_dict()
            else:
                params['three_uid'] = self.three_uid
        if self.two_open_id:
            if hasattr(self.two_open_id, 'to_alipay_dict'):
                params['two_open_id'] = self.two_open_id.to_alipay_dict()
            else:
                params['two_open_id'] = self.two_open_id
        if self.two_uid:
            if hasattr(self.two_uid, 'to_alipay_dict'):
                params['two_uid'] = self.two_uid.to_alipay_dict()
            else:
                params['two_uid'] = self.two_uid
        if self.uid_list:
            if isinstance(self.uid_list, list):
                for i in range(0, len(self.uid_list)):
                    element = self.uid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.uid_list[i] = element.to_alipay_dict()
            if hasattr(self.uid_list, 'to_alipay_dict'):
                params['uid_list'] = self.uid_list.to_alipay_dict()
            else:
                params['uid_list'] = self.uid_list
        if self.uid_list_open_id_list:
            if isinstance(self.uid_list_open_id_list, list):
                for i in range(0, len(self.uid_list_open_id_list)):
                    element = self.uid_list_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.uid_list_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.uid_list_open_id_list, 'to_alipay_dict'):
                params['uid_list_open_id_list'] = self.uid_list_open_id_list.to_alipay_dict()
            else:
                params['uid_list_open_id_list'] = self.uid_list_open_id_list
        if self.user_detail:
            if hasattr(self.user_detail, 'to_alipay_dict'):
                params['user_detail'] = self.user_detail.to_alipay_dict()
            else:
                params['user_detail'] = self.user_detail
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockOpenidtestingQueryModel()
        if 'appid_one' in d:
            o.appid_one = d['appid_one']
        if 'appid_out_one' in d:
            o.appid_out_one = d['appid_out_one']
        if 'appid_out_three' in d:
            o.appid_out_three = d['appid_out_three']
        if 'appid_out_two' in d:
            o.appid_out_two = d['appid_out_two']
        if 'appid_three' in d:
            o.appid_three = d['appid_three']
        if 'appid_two' in d:
            o.appid_two = d['appid_two']
        if 'extra_json' in d:
            o.extra_json = d['extra_json']
        if 'extra_json_1' in d:
            o.extra_json_1 = d['extra_json_1']
        if 'lalala_openid' in d:
            o.lalala_openid = d['lalala_openid']
        if 'lalala_real_open_id' in d:
            o.lalala_real_open_id = d['lalala_real_open_id']
        if 'lalalala' in d:
            o.lalalala = d['lalalala']
        if 'one_open_id' in d:
            o.one_open_id = d['one_open_id']
        if 'one_uid' in d:
            o.one_uid = d['one_uid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'result_oneuid_original' in d:
            o.result_oneuid_original = d['result_oneuid_original']
        if 'test' in d:
            o.test = d['test']
        if 'test_json' in d:
            o.test_json = d['test_json']
        if 'test_wrong' in d:
            o.test_wrong = d['test_wrong']
        if 'three_open_id' in d:
            o.three_open_id = d['three_open_id']
        if 'three_uid' in d:
            o.three_uid = d['three_uid']
        if 'two_open_id' in d:
            o.two_open_id = d['two_open_id']
        if 'two_uid' in d:
            o.two_uid = d['two_uid']
        if 'uid_list' in d:
            o.uid_list = d['uid_list']
        if 'uid_list_open_id_list' in d:
            o.uid_list_open_id_list = d['uid_list_open_id_list']
        if 'user_detail' in d:
            o.user_detail = d['user_detail']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


