#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDecorationFeedsFeedbackSyncModel(object):

    def __init__(self):
        self._assign_reason = None
        self._company_id = None
        self._company_ids = None
        self._company_name = None
        self._feedback_type = None
        self._lead_id = None
        self._provider_id = None
        self._remark = None
        self._status = None
        self._valid = None

    @property
    def assign_reason(self):
        return self._assign_reason

    @assign_reason.setter
    def assign_reason(self, value):
        self._assign_reason = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def company_ids(self):
        return self._company_ids

    @company_ids.setter
    def company_ids(self, value):
        if isinstance(value, list):
            self._company_ids = list()
            for i in value:
                self._company_ids.append(i)
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def feedback_type(self):
        return self._feedback_type

    @feedback_type.setter
    def feedback_type(self, value):
        self._feedback_type = value
    @property
    def lead_id(self):
        return self._lead_id

    @lead_id.setter
    def lead_id(self, value):
        self._lead_id = value
    @property
    def provider_id(self):
        return self._provider_id

    @provider_id.setter
    def provider_id(self, value):
        self._provider_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_reason:
            if hasattr(self.assign_reason, 'to_alipay_dict'):
                params['assign_reason'] = self.assign_reason.to_alipay_dict()
            else:
                params['assign_reason'] = self.assign_reason
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.company_ids:
            if isinstance(self.company_ids, list):
                for i in range(0, len(self.company_ids)):
                    element = self.company_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_ids[i] = element.to_alipay_dict()
            if hasattr(self.company_ids, 'to_alipay_dict'):
                params['company_ids'] = self.company_ids.to_alipay_dict()
            else:
                params['company_ids'] = self.company_ids
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.feedback_type:
            if hasattr(self.feedback_type, 'to_alipay_dict'):
                params['feedback_type'] = self.feedback_type.to_alipay_dict()
            else:
                params['feedback_type'] = self.feedback_type
        if self.lead_id:
            if hasattr(self.lead_id, 'to_alipay_dict'):
                params['lead_id'] = self.lead_id.to_alipay_dict()
            else:
                params['lead_id'] = self.lead_id
        if self.provider_id:
            if hasattr(self.provider_id, 'to_alipay_dict'):
                params['provider_id'] = self.provider_id.to_alipay_dict()
            else:
                params['provider_id'] = self.provider_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.valid:
            if hasattr(self.valid, 'to_alipay_dict'):
                params['valid'] = self.valid.to_alipay_dict()
            else:
                params['valid'] = self.valid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDecorationFeedsFeedbackSyncModel()
        if 'assign_reason' in d:
            o.assign_reason = d['assign_reason']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'company_ids' in d:
            o.company_ids = d['company_ids']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'feedback_type' in d:
            o.feedback_type = d['feedback_type']
        if 'lead_id' in d:
            o.lead_id = d['lead_id']
        if 'provider_id' in d:
            o.provider_id = d['provider_id']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        if 'valid' in d:
            o.valid = d['valid']
        return o


