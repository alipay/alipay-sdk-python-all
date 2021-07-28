#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfarmProjectTargetInfo(object):

    def __init__(self):
        self._current_donation_count = None
        self._donation_target_id = None
        self._donation_target_name = None
        self._quota = None

    @property
    def current_donation_count(self):
        return self._current_donation_count

    @current_donation_count.setter
    def current_donation_count(self, value):
        self._current_donation_count = value
    @property
    def donation_target_id(self):
        return self._donation_target_id

    @donation_target_id.setter
    def donation_target_id(self, value):
        self._donation_target_id = value
    @property
    def donation_target_name(self):
        return self._donation_target_name

    @donation_target_name.setter
    def donation_target_name(self, value):
        self._donation_target_name = value
    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        self._quota = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_donation_count:
            if hasattr(self.current_donation_count, 'to_alipay_dict'):
                params['current_donation_count'] = self.current_donation_count.to_alipay_dict()
            else:
                params['current_donation_count'] = self.current_donation_count
        if self.donation_target_id:
            if hasattr(self.donation_target_id, 'to_alipay_dict'):
                params['donation_target_id'] = self.donation_target_id.to_alipay_dict()
            else:
                params['donation_target_id'] = self.donation_target_id
        if self.donation_target_name:
            if hasattr(self.donation_target_name, 'to_alipay_dict'):
                params['donation_target_name'] = self.donation_target_name.to_alipay_dict()
            else:
                params['donation_target_name'] = self.donation_target_name
        if self.quota:
            if hasattr(self.quota, 'to_alipay_dict'):
                params['quota'] = self.quota.to_alipay_dict()
            else:
                params['quota'] = self.quota
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfarmProjectTargetInfo()
        if 'current_donation_count' in d:
            o.current_donation_count = d['current_donation_count']
        if 'donation_target_id' in d:
            o.donation_target_id = d['donation_target_id']
        if 'donation_target_name' in d:
            o.donation_target_name = d['donation_target_name']
        if 'quota' in d:
            o.quota = d['quota']
        return o


