#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerBehaviorSyncModel(object):

    def __init__(self):
        self._behavior = None
        self._behavior_content = None
        self._contract_no = None
        self._gmt_service = None
        self._principal_type = None
        self._service_id = None
        self._subject_id = None
        self._transaction_id = None
        self._user_id = None

    @property
    def behavior(self):
        return self._behavior

    @behavior.setter
    def behavior(self, value):
        if isinstance(value, list):
            self._behavior = list()
            for i in value:
                self._behavior.append(i)
    @property
    def behavior_content(self):
        return self._behavior_content

    @behavior_content.setter
    def behavior_content(self, value):
        self._behavior_content = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.behavior:
            if isinstance(self.behavior, list):
                for i in range(0, len(self.behavior)):
                    element = self.behavior[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.behavior[i] = element.to_alipay_dict()
            if hasattr(self.behavior, 'to_alipay_dict'):
                params['behavior'] = self.behavior.to_alipay_dict()
            else:
                params['behavior'] = self.behavior
        if self.behavior_content:
            if hasattr(self.behavior_content, 'to_alipay_dict'):
                params['behavior_content'] = self.behavior_content.to_alipay_dict()
            else:
                params['behavior_content'] = self.behavior_content
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.subject_id:
            if hasattr(self.subject_id, 'to_alipay_dict'):
                params['subject_id'] = self.subject_id.to_alipay_dict()
            else:
                params['subject_id'] = self.subject_id
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
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
        o = ZhimaCustomerBehaviorSyncModel()
        if 'behavior' in d:
            o.behavior = d['behavior']
        if 'behavior_content' in d:
            o.behavior_content = d['behavior_content']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'subject_id' in d:
            o.subject_id = d['subject_id']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


