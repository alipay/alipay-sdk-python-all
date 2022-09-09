#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotroomdeviceEventSendModel(object):

    def __init__(self):
        self._biztid = None
        self._door_state = None
        self._face_id = None
        self._reason = None
        self._request_id = None

    @property
    def biztid(self):
        return self._biztid

    @biztid.setter
    def biztid(self, value):
        self._biztid = value
    @property
    def door_state(self):
        return self._door_state

    @door_state.setter
    def door_state(self, value):
        self._door_state = value
    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biztid:
            if hasattr(self.biztid, 'to_alipay_dict'):
                params['biztid'] = self.biztid.to_alipay_dict()
            else:
                params['biztid'] = self.biztid
        if self.door_state:
            if hasattr(self.door_state, 'to_alipay_dict'):
                params['door_state'] = self.door_state.to_alipay_dict()
            else:
                params['door_state'] = self.door_state
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
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
        o = AlipayOpenIotroomdeviceEventSendModel()
        if 'biztid' in d:
            o.biztid = d['biztid']
        if 'door_state' in d:
            o.door_state = d['door_state']
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'reason' in d:
            o.reason = d['reason']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


