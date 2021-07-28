#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BccEventDetail(object):

    def __init__(self):
        self._activity_id = None
        self._complete_tag = None
        self._contract_no = None
        self._event_conent = None
        self._event_day = None
        self._event_type = None
        self._gm_create = None
        self._sign_principal_id = None
        self._zm_role_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def complete_tag(self):
        return self._complete_tag

    @complete_tag.setter
    def complete_tag(self, value):
        self._complete_tag = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def event_conent(self):
        return self._event_conent

    @event_conent.setter
    def event_conent(self, value):
        self._event_conent = value
    @property
    def event_day(self):
        return self._event_day

    @event_day.setter
    def event_day(self, value):
        self._event_day = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def gm_create(self):
        return self._gm_create

    @gm_create.setter
    def gm_create(self, value):
        self._gm_create = value
    @property
    def sign_principal_id(self):
        return self._sign_principal_id

    @sign_principal_id.setter
    def sign_principal_id(self, value):
        self._sign_principal_id = value
    @property
    def zm_role_id(self):
        return self._zm_role_id

    @zm_role_id.setter
    def zm_role_id(self, value):
        self._zm_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.complete_tag:
            if hasattr(self.complete_tag, 'to_alipay_dict'):
                params['complete_tag'] = self.complete_tag.to_alipay_dict()
            else:
                params['complete_tag'] = self.complete_tag
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.event_conent:
            if hasattr(self.event_conent, 'to_alipay_dict'):
                params['event_conent'] = self.event_conent.to_alipay_dict()
            else:
                params['event_conent'] = self.event_conent
        if self.event_day:
            if hasattr(self.event_day, 'to_alipay_dict'):
                params['event_day'] = self.event_day.to_alipay_dict()
            else:
                params['event_day'] = self.event_day
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.gm_create:
            if hasattr(self.gm_create, 'to_alipay_dict'):
                params['gm_create'] = self.gm_create.to_alipay_dict()
            else:
                params['gm_create'] = self.gm_create
        if self.sign_principal_id:
            if hasattr(self.sign_principal_id, 'to_alipay_dict'):
                params['sign_principal_id'] = self.sign_principal_id.to_alipay_dict()
            else:
                params['sign_principal_id'] = self.sign_principal_id
        if self.zm_role_id:
            if hasattr(self.zm_role_id, 'to_alipay_dict'):
                params['zm_role_id'] = self.zm_role_id.to_alipay_dict()
            else:
                params['zm_role_id'] = self.zm_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BccEventDetail()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'complete_tag' in d:
            o.complete_tag = d['complete_tag']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'event_conent' in d:
            o.event_conent = d['event_conent']
        if 'event_day' in d:
            o.event_day = d['event_day']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'gm_create' in d:
            o.gm_create = d['gm_create']
        if 'sign_principal_id' in d:
            o.sign_principal_id = d['sign_principal_id']
        if 'zm_role_id' in d:
            o.zm_role_id = d['zm_role_id']
        return o


