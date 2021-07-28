#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerFulfillmentSyncModel(object):

    def __init__(self):
        self._ext_info = None
        self._gmt_service = None
        self._service_id = None
        self._subject_delta_num = None
        self._subject_id = None
        self._subject_type = None
        self._transaction_id = None
        self._user_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def subject_delta_num(self):
        return self._subject_delta_num

    @subject_delta_num.setter
    def subject_delta_num(self, value):
        self._subject_delta_num = value
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value
    @property
    def subject_type(self):
        return self._subject_type

    @subject_type.setter
    def subject_type(self, value):
        self._subject_type = value
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
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.subject_delta_num:
            if hasattr(self.subject_delta_num, 'to_alipay_dict'):
                params['subject_delta_num'] = self.subject_delta_num.to_alipay_dict()
            else:
                params['subject_delta_num'] = self.subject_delta_num
        if self.subject_id:
            if hasattr(self.subject_id, 'to_alipay_dict'):
                params['subject_id'] = self.subject_id.to_alipay_dict()
            else:
                params['subject_id'] = self.subject_id
        if self.subject_type:
            if hasattr(self.subject_type, 'to_alipay_dict'):
                params['subject_type'] = self.subject_type.to_alipay_dict()
            else:
                params['subject_type'] = self.subject_type
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
        o = ZhimaCustomerFulfillmentSyncModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'subject_delta_num' in d:
            o.subject_delta_num = d['subject_delta_num']
        if 'subject_id' in d:
            o.subject_id = d['subject_id']
        if 'subject_type' in d:
            o.subject_type = d['subject_type']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


