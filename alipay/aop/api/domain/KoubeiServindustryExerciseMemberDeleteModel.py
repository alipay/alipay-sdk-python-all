#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiServindustryExerciseMemberDeleteModel(object):

    def __init__(self):
        self._external_member_id = None
        self._fitness_id = None
        self._member_id = None
        self._request_id = None

    @property
    def external_member_id(self):
        return self._external_member_id

    @external_member_id.setter
    def external_member_id(self, value):
        self._external_member_id = value
    @property
    def fitness_id(self):
        return self._fitness_id

    @fitness_id.setter
    def fitness_id(self, value):
        self._fitness_id = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_member_id:
            if hasattr(self.external_member_id, 'to_alipay_dict'):
                params['external_member_id'] = self.external_member_id.to_alipay_dict()
            else:
                params['external_member_id'] = self.external_member_id
        if self.fitness_id:
            if hasattr(self.fitness_id, 'to_alipay_dict'):
                params['fitness_id'] = self.fitness_id.to_alipay_dict()
            else:
                params['fitness_id'] = self.fitness_id
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryExerciseMemberDeleteModel()
        if 'external_member_id' in d:
            o.external_member_id = d['external_member_id']
        if 'fitness_id' in d:
            o.fitness_id = d['fitness_id']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


