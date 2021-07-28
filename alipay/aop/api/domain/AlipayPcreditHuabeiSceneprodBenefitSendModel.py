#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiSceneprodBenefitSendModel(object):

    def __init__(self):
        self._benefit_channel = None
        self._benefit_id = None
        self._benefit_type = None
        self._biz_date = None
        self._biz_scene = None
        self._instance_id = None
        self._memo = None
        self._out_request_no = None
        self._partner_id = None
        self._request_from = None
        self._security_content = None
        self._user_id = None

    @property
    def benefit_channel(self):
        return self._benefit_channel

    @benefit_channel.setter
    def benefit_channel(self, value):
        self._benefit_channel = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value
    @property
    def security_content(self):
        return self._security_content

    @security_content.setter
    def security_content(self, value):
        self._security_content = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_channel:
            if hasattr(self.benefit_channel, 'to_alipay_dict'):
                params['benefit_channel'] = self.benefit_channel.to_alipay_dict()
            else:
                params['benefit_channel'] = self.benefit_channel
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        if self.security_content:
            if hasattr(self.security_content, 'to_alipay_dict'):
                params['security_content'] = self.security_content.to_alipay_dict()
            else:
                params['security_content'] = self.security_content
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
        o = AlipayPcreditHuabeiSceneprodBenefitSendModel()
        if 'benefit_channel' in d:
            o.benefit_channel = d['benefit_channel']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'request_from' in d:
            o.request_from = d['request_from']
        if 'security_content' in d:
            o.security_content = d['security_content']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


