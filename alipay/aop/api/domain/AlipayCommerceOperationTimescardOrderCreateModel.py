#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VirtualItemOrderExtInfo import VirtualItemOrderExtInfo


class AlipayCommerceOperationTimescardOrderCreateModel(object):

    def __init__(self):
        self._extend_info = None
        self._isv_partner_id = None
        self._item_id = None
        self._out_biz_no = None
        self._partner_id = None
        self._scene_code = None
        self._user_id = None

    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        if isinstance(value, VirtualItemOrderExtInfo):
            self._extend_info = value
        else:
            self._extend_info = VirtualItemOrderExtInfo.from_alipay_dict(value)
    @property
    def isv_partner_id(self):
        return self._isv_partner_id

    @isv_partner_id.setter
    def isv_partner_id(self, value):
        self._isv_partner_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.isv_partner_id:
            if hasattr(self.isv_partner_id, 'to_alipay_dict'):
                params['isv_partner_id'] = self.isv_partner_id.to_alipay_dict()
            else:
                params['isv_partner_id'] = self.isv_partner_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
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
        o = AlipayCommerceOperationTimescardOrderCreateModel()
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'isv_partner_id' in d:
            o.isv_partner_id = d['isv_partner_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


