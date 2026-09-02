#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeUserChangeSyncModel(object):

    def __init__(self):
        self._credit_agreement_id = None
        self._evaluate_time = None
        self._is_new_open = None
        self._open_id = None
        self._out_request_no = None
        self._score_level = None
        self._service_id = None
        self._user_id = None
        self._user_score = None

    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def evaluate_time(self):
        return self._evaluate_time

    @evaluate_time.setter
    def evaluate_time(self, value):
        self._evaluate_time = value
    @property
    def is_new_open(self):
        return self._is_new_open

    @is_new_open.setter
    def is_new_open(self, value):
        self._is_new_open = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def score_level(self):
        return self._score_level

    @score_level.setter
    def score_level(self, value):
        self._score_level = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_score(self):
        return self._user_score

    @user_score.setter
    def user_score(self, value):
        self._user_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_agreement_id:
            if hasattr(self.credit_agreement_id, 'to_alipay_dict'):
                params['credit_agreement_id'] = self.credit_agreement_id.to_alipay_dict()
            else:
                params['credit_agreement_id'] = self.credit_agreement_id
        if self.evaluate_time:
            if hasattr(self.evaluate_time, 'to_alipay_dict'):
                params['evaluate_time'] = self.evaluate_time.to_alipay_dict()
            else:
                params['evaluate_time'] = self.evaluate_time
        if self.is_new_open:
            if hasattr(self.is_new_open, 'to_alipay_dict'):
                params['is_new_open'] = self.is_new_open.to_alipay_dict()
            else:
                params['is_new_open'] = self.is_new_open
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.score_level:
            if hasattr(self.score_level, 'to_alipay_dict'):
                params['score_level'] = self.score_level.to_alipay_dict()
            else:
                params['score_level'] = self.score_level
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_score:
            if hasattr(self.user_score, 'to_alipay_dict'):
                params['user_score'] = self.user_score.to_alipay_dict()
            else:
                params['user_score'] = self.user_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeUserChangeSyncModel()
        if 'credit_agreement_id' in d:
            o.credit_agreement_id = d['credit_agreement_id']
        if 'evaluate_time' in d:
            o.evaluate_time = d['evaluate_time']
        if 'is_new_open' in d:
            o.is_new_open = d['is_new_open']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'score_level' in d:
            o.score_level = d['score_level']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_score' in d:
            o.user_score = d['user_score']
        return o


