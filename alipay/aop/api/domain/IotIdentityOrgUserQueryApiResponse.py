#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotIdentityOrgUserQueryApiResponse(object):

    def __init__(self):
        self._face_id = None
        self._state = None
        self._user_id = None

    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
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
        o = IotIdentityOrgUserQueryApiResponse()
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'state' in d:
            o.state = d['state']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


