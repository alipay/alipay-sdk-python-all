#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderExpoNfccheckinSubmitModel(object):

    def __init__(self):
        self._activity_code = None
        self._check_place = None
        self._check_template_type = None
        self._external_place_mark = None
        self._open_id = None
        self._request_src = None
        self._solution_config_code = None
        self._trade_no = None
        self._user_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def check_place(self):
        return self._check_place

    @check_place.setter
    def check_place(self, value):
        self._check_place = value
    @property
    def check_template_type(self):
        return self._check_template_type

    @check_template_type.setter
    def check_template_type(self, value):
        self._check_template_type = value
    @property
    def external_place_mark(self):
        return self._external_place_mark

    @external_place_mark.setter
    def external_place_mark(self, value):
        self._external_place_mark = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def request_src(self):
        return self._request_src

    @request_src.setter
    def request_src(self, value):
        self._request_src = value
    @property
    def solution_config_code(self):
        return self._solution_config_code

    @solution_config_code.setter
    def solution_config_code(self, value):
        self._solution_config_code = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.check_place:
            if hasattr(self.check_place, 'to_alipay_dict'):
                params['check_place'] = self.check_place.to_alipay_dict()
            else:
                params['check_place'] = self.check_place
        if self.check_template_type:
            if hasattr(self.check_template_type, 'to_alipay_dict'):
                params['check_template_type'] = self.check_template_type.to_alipay_dict()
            else:
                params['check_template_type'] = self.check_template_type
        if self.external_place_mark:
            if hasattr(self.external_place_mark, 'to_alipay_dict'):
                params['external_place_mark'] = self.external_place_mark.to_alipay_dict()
            else:
                params['external_place_mark'] = self.external_place_mark
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.request_src:
            if hasattr(self.request_src, 'to_alipay_dict'):
                params['request_src'] = self.request_src.to_alipay_dict()
            else:
                params['request_src'] = self.request_src
        if self.solution_config_code:
            if hasattr(self.solution_config_code, 'to_alipay_dict'):
                params['solution_config_code'] = self.solution_config_code.to_alipay_dict()
            else:
                params['solution_config_code'] = self.solution_config_code
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AlipayOfflineProviderExpoNfccheckinSubmitModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'check_place' in d:
            o.check_place = d['check_place']
        if 'check_template_type' in d:
            o.check_template_type = d['check_template_type']
        if 'external_place_mark' in d:
            o.external_place_mark = d['external_place_mark']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'request_src' in d:
            o.request_src = d['request_src']
        if 'solution_config_code' in d:
            o.solution_config_code = d['solution_config_code']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


