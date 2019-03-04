#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignMemberTemplateOnlineModel(object):

    def __init__(self):
        self._member_template_id = None
        self._request_id = None

    @property
    def member_template_id(self):
        return self._member_template_id

    @member_template_id.setter
    def member_template_id(self, value):
        self._member_template_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_template_id:
            if hasattr(self.member_template_id, 'to_alipay_dict'):
                params['member_template_id'] = self.member_template_id.to_alipay_dict()
            else:
                params['member_template_id'] = self.member_template_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignMemberTemplateOnlineModel()
        if 'member_template_id' in d:
            o.member_template_id = d['member_template_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


