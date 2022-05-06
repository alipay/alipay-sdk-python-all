#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundIdentitypayMemberUnsignModel(object):

    def __init__(self):
        self._biz_scene = None
        self._member_name = None
        self._out_member_id = None
        self._out_org_id = None
        self._product_code = None
        self._sub_biz_scene = None
        self._user_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def member_name(self):
        return self._member_name

    @member_name.setter
    def member_name(self, value):
        self._member_name = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        self._out_member_id = value
    @property
    def out_org_id(self):
        return self._out_org_id

    @out_org_id.setter
    def out_org_id(self, value):
        self._out_org_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.member_name:
            if hasattr(self.member_name, 'to_alipay_dict'):
                params['member_name'] = self.member_name.to_alipay_dict()
            else:
                params['member_name'] = self.member_name
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.out_org_id:
            if hasattr(self.out_org_id, 'to_alipay_dict'):
                params['out_org_id'] = self.out_org_id.to_alipay_dict()
            else:
                params['out_org_id'] = self.out_org_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
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
        o = AlipayFundIdentitypayMemberUnsignModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'member_name' in d:
            o.member_name = d['member_name']
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'out_org_id' in d:
            o.out_org_id = d['out_org_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


