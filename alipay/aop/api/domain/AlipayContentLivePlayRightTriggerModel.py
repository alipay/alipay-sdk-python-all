#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LivePlayRightDetail import LivePlayRightDetail


class AlipayContentLivePlayRightTriggerModel(object):

    def __init__(self):
        self._alipay_live_id = None
        self._anchor_public_id = None
        self._award_id = None
        self._deliver_type = None
        self._domain = None
        self._out_biz_id = None
        self._right_detail = None
        self._right_type = None
        self._user_public_id = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def anchor_public_id(self):
        return self._anchor_public_id

    @anchor_public_id.setter
    def anchor_public_id(self, value):
        self._anchor_public_id = value
    @property
    def award_id(self):
        return self._award_id

    @award_id.setter
    def award_id(self, value):
        self._award_id = value
    @property
    def deliver_type(self):
        return self._deliver_type

    @deliver_type.setter
    def deliver_type(self, value):
        self._deliver_type = value
    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def right_detail(self):
        return self._right_detail

    @right_detail.setter
    def right_detail(self, value):
        if isinstance(value, LivePlayRightDetail):
            self._right_detail = value
        else:
            self._right_detail = LivePlayRightDetail.from_alipay_dict(value)
    @property
    def right_type(self):
        return self._right_type

    @right_type.setter
    def right_type(self, value):
        self._right_type = value
    @property
    def user_public_id(self):
        return self._user_public_id

    @user_public_id.setter
    def user_public_id(self, value):
        self._user_public_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_live_id:
            if hasattr(self.alipay_live_id, 'to_alipay_dict'):
                params['alipay_live_id'] = self.alipay_live_id.to_alipay_dict()
            else:
                params['alipay_live_id'] = self.alipay_live_id
        if self.anchor_public_id:
            if hasattr(self.anchor_public_id, 'to_alipay_dict'):
                params['anchor_public_id'] = self.anchor_public_id.to_alipay_dict()
            else:
                params['anchor_public_id'] = self.anchor_public_id
        if self.award_id:
            if hasattr(self.award_id, 'to_alipay_dict'):
                params['award_id'] = self.award_id.to_alipay_dict()
            else:
                params['award_id'] = self.award_id
        if self.deliver_type:
            if hasattr(self.deliver_type, 'to_alipay_dict'):
                params['deliver_type'] = self.deliver_type.to_alipay_dict()
            else:
                params['deliver_type'] = self.deliver_type
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.right_detail:
            if hasattr(self.right_detail, 'to_alipay_dict'):
                params['right_detail'] = self.right_detail.to_alipay_dict()
            else:
                params['right_detail'] = self.right_detail
        if self.right_type:
            if hasattr(self.right_type, 'to_alipay_dict'):
                params['right_type'] = self.right_type.to_alipay_dict()
            else:
                params['right_type'] = self.right_type
        if self.user_public_id:
            if hasattr(self.user_public_id, 'to_alipay_dict'):
                params['user_public_id'] = self.user_public_id.to_alipay_dict()
            else:
                params['user_public_id'] = self.user_public_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLivePlayRightTriggerModel()
        if 'alipay_live_id' in d:
            o.alipay_live_id = d['alipay_live_id']
        if 'anchor_public_id' in d:
            o.anchor_public_id = d['anchor_public_id']
        if 'award_id' in d:
            o.award_id = d['award_id']
        if 'deliver_type' in d:
            o.deliver_type = d['deliver_type']
        if 'domain' in d:
            o.domain = d['domain']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'right_detail' in d:
            o.right_detail = d['right_detail']
        if 'right_type' in d:
            o.right_type = d['right_type']
        if 'user_public_id' in d:
            o.user_public_id = d['user_public_id']
        return o


