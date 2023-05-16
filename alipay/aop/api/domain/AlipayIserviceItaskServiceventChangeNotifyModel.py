#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceItaskServiceventChangeNotifyModel(object):

    def __init__(self):
        self._customer_identity = None
        self._customer_identity_type = None
        self._memo = None
        self._org_id = None
        self._org_name = None
        self._out_action_type = None
        self._out_biz_no = None
        self._out_service_assess = None
        self._out_service_end_time = None
        self._out_service_record_id = None
        self._out_service_start_time = None
        self._out_service_state = None
        self._out_service_type = None
        self._summary = None
        self._transfer_source = None

    @property
    def customer_identity(self):
        return self._customer_identity

    @customer_identity.setter
    def customer_identity(self, value):
        self._customer_identity = value
    @property
    def customer_identity_type(self):
        return self._customer_identity_type

    @customer_identity_type.setter
    def customer_identity_type(self, value):
        self._customer_identity_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def out_action_type(self):
        return self._out_action_type

    @out_action_type.setter
    def out_action_type(self, value):
        self._out_action_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_service_assess(self):
        return self._out_service_assess

    @out_service_assess.setter
    def out_service_assess(self, value):
        self._out_service_assess = value
    @property
    def out_service_end_time(self):
        return self._out_service_end_time

    @out_service_end_time.setter
    def out_service_end_time(self, value):
        self._out_service_end_time = value
    @property
    def out_service_record_id(self):
        return self._out_service_record_id

    @out_service_record_id.setter
    def out_service_record_id(self, value):
        self._out_service_record_id = value
    @property
    def out_service_start_time(self):
        return self._out_service_start_time

    @out_service_start_time.setter
    def out_service_start_time(self, value):
        self._out_service_start_time = value
    @property
    def out_service_state(self):
        return self._out_service_state

    @out_service_state.setter
    def out_service_state(self, value):
        self._out_service_state = value
    @property
    def out_service_type(self):
        return self._out_service_type

    @out_service_type.setter
    def out_service_type(self, value):
        self._out_service_type = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def transfer_source(self):
        return self._transfer_source

    @transfer_source.setter
    def transfer_source(self, value):
        self._transfer_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_identity:
            if hasattr(self.customer_identity, 'to_alipay_dict'):
                params['customer_identity'] = self.customer_identity.to_alipay_dict()
            else:
                params['customer_identity'] = self.customer_identity
        if self.customer_identity_type:
            if hasattr(self.customer_identity_type, 'to_alipay_dict'):
                params['customer_identity_type'] = self.customer_identity_type.to_alipay_dict()
            else:
                params['customer_identity_type'] = self.customer_identity_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.out_action_type:
            if hasattr(self.out_action_type, 'to_alipay_dict'):
                params['out_action_type'] = self.out_action_type.to_alipay_dict()
            else:
                params['out_action_type'] = self.out_action_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_service_assess:
            if hasattr(self.out_service_assess, 'to_alipay_dict'):
                params['out_service_assess'] = self.out_service_assess.to_alipay_dict()
            else:
                params['out_service_assess'] = self.out_service_assess
        if self.out_service_end_time:
            if hasattr(self.out_service_end_time, 'to_alipay_dict'):
                params['out_service_end_time'] = self.out_service_end_time.to_alipay_dict()
            else:
                params['out_service_end_time'] = self.out_service_end_time
        if self.out_service_record_id:
            if hasattr(self.out_service_record_id, 'to_alipay_dict'):
                params['out_service_record_id'] = self.out_service_record_id.to_alipay_dict()
            else:
                params['out_service_record_id'] = self.out_service_record_id
        if self.out_service_start_time:
            if hasattr(self.out_service_start_time, 'to_alipay_dict'):
                params['out_service_start_time'] = self.out_service_start_time.to_alipay_dict()
            else:
                params['out_service_start_time'] = self.out_service_start_time
        if self.out_service_state:
            if hasattr(self.out_service_state, 'to_alipay_dict'):
                params['out_service_state'] = self.out_service_state.to_alipay_dict()
            else:
                params['out_service_state'] = self.out_service_state
        if self.out_service_type:
            if hasattr(self.out_service_type, 'to_alipay_dict'):
                params['out_service_type'] = self.out_service_type.to_alipay_dict()
            else:
                params['out_service_type'] = self.out_service_type
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.transfer_source:
            if hasattr(self.transfer_source, 'to_alipay_dict'):
                params['transfer_source'] = self.transfer_source.to_alipay_dict()
            else:
                params['transfer_source'] = self.transfer_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskServiceventChangeNotifyModel()
        if 'customer_identity' in d:
            o.customer_identity = d['customer_identity']
        if 'customer_identity_type' in d:
            o.customer_identity_type = d['customer_identity_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'out_action_type' in d:
            o.out_action_type = d['out_action_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_service_assess' in d:
            o.out_service_assess = d['out_service_assess']
        if 'out_service_end_time' in d:
            o.out_service_end_time = d['out_service_end_time']
        if 'out_service_record_id' in d:
            o.out_service_record_id = d['out_service_record_id']
        if 'out_service_start_time' in d:
            o.out_service_start_time = d['out_service_start_time']
        if 'out_service_state' in d:
            o.out_service_state = d['out_service_state']
        if 'out_service_type' in d:
            o.out_service_type = d['out_service_type']
        if 'summary' in d:
            o.summary = d['summary']
        if 'transfer_source' in d:
            o.transfer_source = d['transfer_source']
        return o


