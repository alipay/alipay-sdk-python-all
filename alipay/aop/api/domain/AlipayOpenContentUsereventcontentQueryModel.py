#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SmartphoneVendorsEventInfo import SmartphoneVendorsEventInfo
from alipay.aop.api.domain.SmartphoneVendorsUserIdentity import SmartphoneVendorsUserIdentity


class AlipayOpenContentUsereventcontentQueryModel(object):

    def __init__(self):
        self._request_id = None
        self._smartphone_vendors_event_info = None
        self._smartphone_vendors_user_identity = None
        self._vendor = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def smartphone_vendors_event_info(self):
        return self._smartphone_vendors_event_info

    @smartphone_vendors_event_info.setter
    def smartphone_vendors_event_info(self, value):
        if isinstance(value, SmartphoneVendorsEventInfo):
            self._smartphone_vendors_event_info = value
        else:
            self._smartphone_vendors_event_info = SmartphoneVendorsEventInfo.from_alipay_dict(value)
    @property
    def smartphone_vendors_user_identity(self):
        return self._smartphone_vendors_user_identity

    @smartphone_vendors_user_identity.setter
    def smartphone_vendors_user_identity(self, value):
        if isinstance(value, SmartphoneVendorsUserIdentity):
            self._smartphone_vendors_user_identity = value
        else:
            self._smartphone_vendors_user_identity = SmartphoneVendorsUserIdentity.from_alipay_dict(value)
    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        self._vendor = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.smartphone_vendors_event_info:
            if hasattr(self.smartphone_vendors_event_info, 'to_alipay_dict'):
                params['smartphone_vendors_event_info'] = self.smartphone_vendors_event_info.to_alipay_dict()
            else:
                params['smartphone_vendors_event_info'] = self.smartphone_vendors_event_info
        if self.smartphone_vendors_user_identity:
            if hasattr(self.smartphone_vendors_user_identity, 'to_alipay_dict'):
                params['smartphone_vendors_user_identity'] = self.smartphone_vendors_user_identity.to_alipay_dict()
            else:
                params['smartphone_vendors_user_identity'] = self.smartphone_vendors_user_identity
        if self.vendor:
            if hasattr(self.vendor, 'to_alipay_dict'):
                params['vendor'] = self.vendor.to_alipay_dict()
            else:
                params['vendor'] = self.vendor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenContentUsereventcontentQueryModel()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'smartphone_vendors_event_info' in d:
            o.smartphone_vendors_event_info = d['smartphone_vendors_event_info']
        if 'smartphone_vendors_user_identity' in d:
            o.smartphone_vendors_user_identity = d['smartphone_vendors_user_identity']
        if 'vendor' in d:
            o.vendor = d['vendor']
        return o


