#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedfollowupBadgeNotifyModel(object):

    def __init__(self):
        self._action = None
        self._aq_pid = None
        self._issue_biz_info = None
        self._issue_body = None
        self._out_biz_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def aq_pid(self):
        return self._aq_pid

    @aq_pid.setter
    def aq_pid(self, value):
        self._aq_pid = value
    @property
    def issue_biz_info(self):
        return self._issue_biz_info

    @issue_biz_info.setter
    def issue_biz_info(self, value):
        self._issue_biz_info = value
    @property
    def issue_body(self):
        return self._issue_body

    @issue_body.setter
    def issue_body(self, value):
        self._issue_body = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.aq_pid:
            if hasattr(self.aq_pid, 'to_alipay_dict'):
                params['aq_pid'] = self.aq_pid.to_alipay_dict()
            else:
                params['aq_pid'] = self.aq_pid
        if self.issue_biz_info:
            if hasattr(self.issue_biz_info, 'to_alipay_dict'):
                params['issue_biz_info'] = self.issue_biz_info.to_alipay_dict()
            else:
                params['issue_biz_info'] = self.issue_biz_info
        if self.issue_body:
            if hasattr(self.issue_body, 'to_alipay_dict'):
                params['issue_body'] = self.issue_body.to_alipay_dict()
            else:
                params['issue_body'] = self.issue_body
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedfollowupBadgeNotifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'aq_pid' in d:
            o.aq_pid = d['aq_pid']
        if 'issue_biz_info' in d:
            o.issue_biz_info = d['issue_biz_info']
        if 'issue_body' in d:
            o.issue_body = d['issue_body']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        return o


