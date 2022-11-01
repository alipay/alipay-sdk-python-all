#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenidComplex import OpenidComplex
from alipay.aop.api.domain.UserDetail import UserDetail


class AlipayOpenOperationOpenbizmockOpenidtestingQueryModel(object):

    def __init__(self):
        self._extra_json = None
        self._extra_json_1 = None
        self._open_id = None
        self._test = None
        self._test_json = None
        self._test_wrong = None
        self._user_detail = None
        self._user_id = None

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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if 'extra_json' in d:
            o.extra_json = d['extra_json']
        if 'extra_json_1' in d:
            o.extra_json_1 = d['extra_json_1']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'test' in d:
            o.test = d['test']
        if 'test_json' in d:
            o.test_json = d['test_json']
        if 'test_wrong' in d:
            o.test_wrong = d['test_wrong']
        if 'user_detail' in d:
            o.user_detail = d['user_detail']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


