#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankEcnyWalletUnbindModel(object):

    def __init__(self):
        self._bind_scene = None
        self._out_request_no = None
        self._wallet_id = None

    @property
    def bind_scene(self):
        return self._bind_scene

    @bind_scene.setter
    def bind_scene(self, value):
        self._bind_scene = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_scene:
            if hasattr(self.bind_scene, 'to_alipay_dict'):
                params['bind_scene'] = self.bind_scene.to_alipay_dict()
            else:
                params['bind_scene'] = self.bind_scene
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.wallet_id:
            if hasattr(self.wallet_id, 'to_alipay_dict'):
                params['wallet_id'] = self.wallet_id.to_alipay_dict()
            else:
                params['wallet_id'] = self.wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyWalletUnbindModel()
        if 'bind_scene' in d:
            o.bind_scene = d['bind_scene']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'wallet_id' in d:
            o.wallet_id = d['wallet_id']
        return o


