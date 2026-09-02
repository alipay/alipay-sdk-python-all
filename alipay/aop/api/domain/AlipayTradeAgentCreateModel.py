#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeAgentCreateModel(object):

    def __init__(self):
        self._attributes = None
        self._carrier = None
        self._logo = None
        self._name = None
        self._out_request_no = None
        self._owner_alipay_account = None
        self._platform = None
        self._sub_name = None

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value
    @property
    def carrier(self):
        return self._carrier

    @carrier.setter
    def carrier(self, value):
        self._carrier = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def owner_alipay_account(self):
        return self._owner_alipay_account

    @owner_alipay_account.setter
    def owner_alipay_account(self, value):
        self._owner_alipay_account = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def sub_name(self):
        return self._sub_name

    @sub_name.setter
    def sub_name(self, value):
        self._sub_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.attributes:
            if hasattr(self.attributes, 'to_alipay_dict'):
                params['attributes'] = self.attributes.to_alipay_dict()
            else:
                params['attributes'] = self.attributes
        if self.carrier:
            if hasattr(self.carrier, 'to_alipay_dict'):
                params['carrier'] = self.carrier.to_alipay_dict()
            else:
                params['carrier'] = self.carrier
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.owner_alipay_account:
            if hasattr(self.owner_alipay_account, 'to_alipay_dict'):
                params['owner_alipay_account'] = self.owner_alipay_account.to_alipay_dict()
            else:
                params['owner_alipay_account'] = self.owner_alipay_account
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.sub_name:
            if hasattr(self.sub_name, 'to_alipay_dict'):
                params['sub_name'] = self.sub_name.to_alipay_dict()
            else:
                params['sub_name'] = self.sub_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeAgentCreateModel()
        if 'attributes' in d:
            o.attributes = d['attributes']
        if 'carrier' in d:
            o.carrier = d['carrier']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'owner_alipay_account' in d:
            o.owner_alipay_account = d['owner_alipay_account']
        if 'platform' in d:
            o.platform = d['platform']
        if 'sub_name' in d:
            o.sub_name = d['sub_name']
        return o


