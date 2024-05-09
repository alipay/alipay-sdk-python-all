#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationCrowdMatchModel(object):

    def __init__(self):
        self._crowd_id = None
        self._user_id = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        if isinstance(value, list):
            self._crowd_id = list()
            for i in value:
                self._crowd_id.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_id:
            if isinstance(self.crowd_id, list):
                for i in range(0, len(self.crowd_id)):
                    element = self.crowd_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crowd_id[i] = element.to_alipay_dict()
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
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
        o = AlipayCommerceAcommunicationCrowdMatchModel()
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


