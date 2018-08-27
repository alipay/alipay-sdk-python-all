#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoUserPointReceiveModel(object):

    def __init__(self):
        self._auto_campaign_type = None
        self._extend_info = None
        self._out_biz_no = None
        self._scene_type = None
        self._user_id = None

    @property
    def auto_campaign_type(self):
        return self._auto_campaign_type

    @auto_campaign_type.setter
    def auto_campaign_type(self, value):
        self._auto_campaign_type = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_campaign_type:
            if hasattr(self.auto_campaign_type, 'to_alipay_dict'):
                params['auto_campaign_type'] = self.auto_campaign_type.to_alipay_dict()
            else:
                params['auto_campaign_type'] = self.auto_campaign_type
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
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
        o = AlipayInsAutoUserPointReceiveModel()
        if 'auto_campaign_type' in d:
            o.auto_campaign_type = d['auto_campaign_type']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


