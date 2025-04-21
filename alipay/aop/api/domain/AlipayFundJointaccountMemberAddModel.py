#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundJointaccountMemberAddModel(object):

    def __init__(self):
        self._biz_scene = None
        self._expire_time = None
        self._invitee_id = None
        self._invitee_type = None
        self._inviter_id = None
        self._inviter_type = None
        self._out_biz_no = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def invitee_id(self):
        return self._invitee_id

    @invitee_id.setter
    def invitee_id(self, value):
        self._invitee_id = value
    @property
    def invitee_type(self):
        return self._invitee_type

    @invitee_type.setter
    def invitee_type(self, value):
        self._invitee_type = value
    @property
    def inviter_id(self):
        return self._inviter_id

    @inviter_id.setter
    def inviter_id(self, value):
        self._inviter_id = value
    @property
    def inviter_type(self):
        return self._inviter_type

    @inviter_type.setter
    def inviter_type(self, value):
        self._inviter_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.invitee_id:
            if hasattr(self.invitee_id, 'to_alipay_dict'):
                params['invitee_id'] = self.invitee_id.to_alipay_dict()
            else:
                params['invitee_id'] = self.invitee_id
        if self.invitee_type:
            if hasattr(self.invitee_type, 'to_alipay_dict'):
                params['invitee_type'] = self.invitee_type.to_alipay_dict()
            else:
                params['invitee_type'] = self.invitee_type
        if self.inviter_id:
            if hasattr(self.inviter_id, 'to_alipay_dict'):
                params['inviter_id'] = self.inviter_id.to_alipay_dict()
            else:
                params['inviter_id'] = self.inviter_id
        if self.inviter_type:
            if hasattr(self.inviter_type, 'to_alipay_dict'):
                params['inviter_type'] = self.inviter_type.to_alipay_dict()
            else:
                params['inviter_type'] = self.inviter_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundJointaccountMemberAddModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'invitee_id' in d:
            o.invitee_id = d['invitee_id']
        if 'invitee_type' in d:
            o.invitee_type = d['invitee_type']
        if 'inviter_id' in d:
            o.inviter_id = d['inviter_id']
        if 'inviter_type' in d:
            o.inviter_type = d['inviter_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


