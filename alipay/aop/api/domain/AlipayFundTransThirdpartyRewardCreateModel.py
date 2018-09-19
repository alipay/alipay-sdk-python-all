#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransThirdpartyRewardCreateModel(object):

    def __init__(self):
        self._amount = None
        self._ext_param = None
        self._out_no = None
        self._receiver_user_id = None
        self._scene = None
        self._sender_user_id = None
        self._title = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def receiver_user_id(self):
        return self._receiver_user_id

    @receiver_user_id.setter
    def receiver_user_id(self, value):
        self._receiver_user_id = value
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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.out_no:
            if hasattr(self.out_no, 'to_alipay_dict'):
                params['out_no'] = self.out_no.to_alipay_dict()
            else:
                params['out_no'] = self.out_no
        if self.receiver_user_id:
            if hasattr(self.receiver_user_id, 'to_alipay_dict'):
                params['receiver_user_id'] = self.receiver_user_id.to_alipay_dict()
            else:
                params['receiver_user_id'] = self.receiver_user_id
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
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransThirdpartyRewardCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'out_no' in d:
            o.out_no = d['out_no']
        if 'receiver_user_id' in d:
            o.receiver_user_id = d['receiver_user_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sender_user_id' in d:
            o.sender_user_id = d['sender_user_id']
        if 'title' in d:
            o.title = d['title']
        return o


