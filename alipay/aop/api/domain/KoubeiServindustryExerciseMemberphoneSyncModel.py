#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiServindustryExerciseMemberphoneSyncModel(object):

    def __init__(self):
        self._phone_list = None
        self._request_id = None

    @property
    def phone_list(self):
        return self._phone_list

    @phone_list.setter
    def phone_list(self, value):
        if isinstance(value, list):
            self._phone_list = list()
            for i in value:
                self._phone_list.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.phone_list:
            if isinstance(self.phone_list, list):
                for i in range(0, len(self.phone_list)):
                    element = self.phone_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone_list[i] = element.to_alipay_dict()
            if hasattr(self.phone_list, 'to_alipay_dict'):
                params['phone_list'] = self.phone_list.to_alipay_dict()
            else:
                params['phone_list'] = self.phone_list
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
        o = KoubeiServindustryExerciseMemberphoneSyncModel()
        if 'phone_list' in d:
            o.phone_list = d['phone_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


