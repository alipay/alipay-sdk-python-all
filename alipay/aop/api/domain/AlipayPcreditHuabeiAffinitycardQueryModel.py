#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiAffinitycardQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_scene = None
        self._open_id = None
        self._user_prod_account_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_prod_account_no(self):
        return self._user_prod_account_no

    @user_prod_account_no.setter
    def user_prod_account_no(self, value):
        self._user_prod_account_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_prod_account_no:
            if hasattr(self.user_prod_account_no, 'to_alipay_dict'):
                params['user_prod_account_no'] = self.user_prod_account_no.to_alipay_dict()
            else:
                params['user_prod_account_no'] = self.user_prod_account_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiAffinitycardQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_prod_account_no' in d:
            o.user_prod_account_no = d['user_prod_account_no']
        return o


