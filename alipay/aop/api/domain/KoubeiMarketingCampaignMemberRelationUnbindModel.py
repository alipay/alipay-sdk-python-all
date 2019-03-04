#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignMemberRelationUnbindModel(object):

    def __init__(self):
        self._member_template_id = None
        self._out_member_no = None
        self._request_id = None
        self._user_id = None

    @property
    def member_template_id(self):
        return self._member_template_id

    @member_template_id.setter
    def member_template_id(self, value):
        self._member_template_id = value
    @property
    def out_member_no(self):
        return self._out_member_no

    @out_member_no.setter
    def out_member_no(self, value):
        self._out_member_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_template_id:
            if hasattr(self.member_template_id, 'to_alipay_dict'):
                params['member_template_id'] = self.member_template_id.to_alipay_dict()
            else:
                params['member_template_id'] = self.member_template_id
        if self.out_member_no:
            if hasattr(self.out_member_no, 'to_alipay_dict'):
                params['out_member_no'] = self.out_member_no.to_alipay_dict()
            else:
                params['out_member_no'] = self.out_member_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        o = KoubeiMarketingCampaignMemberRelationUnbindModel()
        if 'member_template_id' in d:
            o.member_template_id = d['member_template_id']
        if 'out_member_no' in d:
            o.out_member_no = d['out_member_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


