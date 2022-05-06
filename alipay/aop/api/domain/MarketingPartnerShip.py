#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MarketingAuthorizedData import MarketingAuthorizedData
from alipay.aop.api.domain.MarketingPartner import MarketingPartner


class MarketingPartnerShip(object):

    def __init__(self):
        self._authorized_data = None
        self._create_time = None
        self._partner = None
        self._status = None
        self._stop_time = None

    @property
    def authorized_data(self):
        return self._authorized_data

    @authorized_data.setter
    def authorized_data(self, value):
        if isinstance(value, MarketingAuthorizedData):
            self._authorized_data = value
        else:
            self._authorized_data = MarketingAuthorizedData.from_alipay_dict(value)
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def partner(self):
        return self._partner

    @partner.setter
    def partner(self, value):
        if isinstance(value, MarketingPartner):
            self._partner = value
        else:
            self._partner = MarketingPartner.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def stop_time(self):
        return self._stop_time

    @stop_time.setter
    def stop_time(self, value):
        self._stop_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_data:
            if hasattr(self.authorized_data, 'to_alipay_dict'):
                params['authorized_data'] = self.authorized_data.to_alipay_dict()
            else:
                params['authorized_data'] = self.authorized_data
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.partner:
            if hasattr(self.partner, 'to_alipay_dict'):
                params['partner'] = self.partner.to_alipay_dict()
            else:
                params['partner'] = self.partner
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.stop_time:
            if hasattr(self.stop_time, 'to_alipay_dict'):
                params['stop_time'] = self.stop_time.to_alipay_dict()
            else:
                params['stop_time'] = self.stop_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketingPartnerShip()
        if 'authorized_data' in d:
            o.authorized_data = d['authorized_data']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'partner' in d:
            o.partner = d['partner']
        if 'status' in d:
            o.status = d['status']
        if 'stop_time' in d:
            o.stop_time = d['stop_time']
        return o


