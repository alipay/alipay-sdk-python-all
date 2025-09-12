#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarLeadsBizstatusSyncModel(object):

    def __init__(self):
        self._leads_biz_code = None
        self._leads_id = None
        self._open_id = None
        self._remark = None
        self._scene_code = None
        self._source_channel = None
        self._user_id = None

    @property
    def leads_biz_code(self):
        return self._leads_biz_code

    @leads_biz_code.setter
    def leads_biz_code(self, value):
        self._leads_biz_code = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def source_channel(self):
        return self._source_channel

    @source_channel.setter
    def source_channel(self, value):
        self._source_channel = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.leads_biz_code:
            if hasattr(self.leads_biz_code, 'to_alipay_dict'):
                params['leads_biz_code'] = self.leads_biz_code.to_alipay_dict()
            else:
                params['leads_biz_code'] = self.leads_biz_code
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.source_channel:
            if hasattr(self.source_channel, 'to_alipay_dict'):
                params['source_channel'] = self.source_channel.to_alipay_dict()
            else:
                params['source_channel'] = self.source_channel
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
        o = AlipayEcoMycarLeadsBizstatusSyncModel()
        if 'leads_biz_code' in d:
            o.leads_biz_code = d['leads_biz_code']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'remark' in d:
            o.remark = d['remark']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'source_channel' in d:
            o.source_channel = d['source_channel']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


