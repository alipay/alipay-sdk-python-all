#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantMemberwalletProductCreateModel(object):

    def __init__(self):
        self._member_wallet_name = None
        self._member_wallet_type = None
        self._out_biz_no = None
        self._out_scene_id = None

    @property
    def member_wallet_name(self):
        return self._member_wallet_name

    @member_wallet_name.setter
    def member_wallet_name(self, value):
        self._member_wallet_name = value
    @property
    def member_wallet_type(self):
        return self._member_wallet_type

    @member_wallet_type.setter
    def member_wallet_type(self, value):
        self._member_wallet_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_scene_id(self):
        return self._out_scene_id

    @out_scene_id.setter
    def out_scene_id(self, value):
        self._out_scene_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_wallet_name:
            if hasattr(self.member_wallet_name, 'to_alipay_dict'):
                params['member_wallet_name'] = self.member_wallet_name.to_alipay_dict()
            else:
                params['member_wallet_name'] = self.member_wallet_name
        if self.member_wallet_type:
            if hasattr(self.member_wallet_type, 'to_alipay_dict'):
                params['member_wallet_type'] = self.member_wallet_type.to_alipay_dict()
            else:
                params['member_wallet_type'] = self.member_wallet_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_scene_id:
            if hasattr(self.out_scene_id, 'to_alipay_dict'):
                params['out_scene_id'] = self.out_scene_id.to_alipay_dict()
            else:
                params['out_scene_id'] = self.out_scene_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantMemberwalletProductCreateModel()
        if 'member_wallet_name' in d:
            o.member_wallet_name = d['member_wallet_name']
        if 'member_wallet_type' in d:
            o.member_wallet_type = d['member_wallet_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_scene_id' in d:
            o.out_scene_id = d['out_scene_id']
        return o


