#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JobIntentionDetail import JobIntentionDetail


class AlipayEbppIndustryJobInvitationSendModel(object):

    def __init__(self):
        self._invite_text = None
        self._job_intention_list = None
        self._mobile = None
        self._out_invitation_id = None
        self._out_job_id = None

    @property
    def invite_text(self):
        return self._invite_text

    @invite_text.setter
    def invite_text(self, value):
        self._invite_text = value
    @property
    def job_intention_list(self):
        return self._job_intention_list

    @job_intention_list.setter
    def job_intention_list(self, value):
        if isinstance(value, list):
            self._job_intention_list = list()
            for i in value:
                if isinstance(i, JobIntentionDetail):
                    self._job_intention_list.append(i)
                else:
                    self._job_intention_list.append(JobIntentionDetail.from_alipay_dict(i))
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_invitation_id(self):
        return self._out_invitation_id

    @out_invitation_id.setter
    def out_invitation_id(self, value):
        self._out_invitation_id = value
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.invite_text:
            if hasattr(self.invite_text, 'to_alipay_dict'):
                params['invite_text'] = self.invite_text.to_alipay_dict()
            else:
                params['invite_text'] = self.invite_text
        if self.job_intention_list:
            if isinstance(self.job_intention_list, list):
                for i in range(0, len(self.job_intention_list)):
                    element = self.job_intention_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_intention_list[i] = element.to_alipay_dict()
            if hasattr(self.job_intention_list, 'to_alipay_dict'):
                params['job_intention_list'] = self.job_intention_list.to_alipay_dict()
            else:
                params['job_intention_list'] = self.job_intention_list
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.out_invitation_id:
            if hasattr(self.out_invitation_id, 'to_alipay_dict'):
                params['out_invitation_id'] = self.out_invitation_id.to_alipay_dict()
            else:
                params['out_invitation_id'] = self.out_invitation_id
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryJobInvitationSendModel()
        if 'invite_text' in d:
            o.invite_text = d['invite_text']
        if 'job_intention_list' in d:
            o.job_intention_list = d['job_intention_list']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_invitation_id' in d:
            o.out_invitation_id = d['out_invitation_id']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        return o


