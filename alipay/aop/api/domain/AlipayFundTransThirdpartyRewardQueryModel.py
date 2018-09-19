#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransThirdpartyRewardQueryModel(object):

    def __init__(self):
        self._scene = None
        self._sender_user_id = None
        self._transfer_no = None

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sender_user_id(self):
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, value):
        self._sender_user_id = value
    @property
    def transfer_no(self):
        return self._transfer_no

    @transfer_no.setter
    def transfer_no(self, value):
        self._transfer_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sender_user_id:
            if hasattr(self.sender_user_id, 'to_alipay_dict'):
                params['sender_user_id'] = self.sender_user_id.to_alipay_dict()
            else:
                params['sender_user_id'] = self.sender_user_id
        if self.transfer_no:
            if hasattr(self.transfer_no, 'to_alipay_dict'):
                params['transfer_no'] = self.transfer_no.to_alipay_dict()
            else:
                params['transfer_no'] = self.transfer_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransThirdpartyRewardQueryModel()
        if 'scene' in d:
            o.scene = d['scene']
        if 'sender_user_id' in d:
            o.sender_user_id = d['sender_user_id']
        if 'transfer_no' in d:
            o.transfer_no = d['transfer_no']
        return o


