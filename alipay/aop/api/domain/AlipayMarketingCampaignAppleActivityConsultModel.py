#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignAppleActivityConsultModel(object):

    def __init__(self):
        self._activity_id = None
        self._extra = None
        self._out_biz_value = None
        self._user_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value):
        self._extra = value
    @property
    def out_biz_value(self):
        return self._out_biz_value

    @out_biz_value.setter
    def out_biz_value(self, value):
        self._out_biz_value = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.extra:
            if hasattr(self.extra, 'to_alipay_dict'):
                params['extra'] = self.extra.to_alipay_dict()
            else:
                params['extra'] = self.extra
        if self.out_biz_value:
            if hasattr(self.out_biz_value, 'to_alipay_dict'):
                params['out_biz_value'] = self.out_biz_value.to_alipay_dict()
            else:
                params['out_biz_value'] = self.out_biz_value
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
        o = AlipayMarketingCampaignAppleActivityConsultModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'extra' in d:
            o.extra = d['extra']
        if 'out_biz_value' in d:
            o.out_biz_value = d['out_biz_value']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


