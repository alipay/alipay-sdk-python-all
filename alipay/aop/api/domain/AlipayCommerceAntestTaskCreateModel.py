#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAntestTaskCreateModel(object):

    def __init__(self):
        self._alipay_version = None
        self._app_code = None
        self._app_version = None
        self._case_list = None
        self._device_strategy = None
        self._mock_group_id = None
        self._product_code = None
        self._test_strategy = None

    @property
    def alipay_version(self):
        return self._alipay_version

    @alipay_version.setter
    def alipay_version(self, value):
        self._alipay_version = value
    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def case_list(self):
        return self._case_list

    @case_list.setter
    def case_list(self, value):
        self._case_list = value
    @property
    def device_strategy(self):
        return self._device_strategy

    @device_strategy.setter
    def device_strategy(self, value):
        self._device_strategy = value
    @property
    def mock_group_id(self):
        return self._mock_group_id

    @mock_group_id.setter
    def mock_group_id(self, value):
        self._mock_group_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def test_strategy(self):
        return self._test_strategy

    @test_strategy.setter
    def test_strategy(self, value):
        self._test_strategy = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_version:
            if hasattr(self.alipay_version, 'to_alipay_dict'):
                params['alipay_version'] = self.alipay_version.to_alipay_dict()
            else:
                params['alipay_version'] = self.alipay_version
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.case_list:
            if hasattr(self.case_list, 'to_alipay_dict'):
                params['case_list'] = self.case_list.to_alipay_dict()
            else:
                params['case_list'] = self.case_list
        if self.device_strategy:
            if hasattr(self.device_strategy, 'to_alipay_dict'):
                params['device_strategy'] = self.device_strategy.to_alipay_dict()
            else:
                params['device_strategy'] = self.device_strategy
        if self.mock_group_id:
            if hasattr(self.mock_group_id, 'to_alipay_dict'):
                params['mock_group_id'] = self.mock_group_id.to_alipay_dict()
            else:
                params['mock_group_id'] = self.mock_group_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.test_strategy:
            if hasattr(self.test_strategy, 'to_alipay_dict'):
                params['test_strategy'] = self.test_strategy.to_alipay_dict()
            else:
                params['test_strategy'] = self.test_strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAntestTaskCreateModel()
        if 'alipay_version' in d:
            o.alipay_version = d['alipay_version']
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'case_list' in d:
            o.case_list = d['case_list']
        if 'device_strategy' in d:
            o.device_strategy = d['device_strategy']
        if 'mock_group_id' in d:
            o.mock_group_id = d['mock_group_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'test_strategy' in d:
            o.test_strategy = d['test_strategy']
        return o


