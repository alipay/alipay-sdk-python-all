#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcbenefitcoreBfactivitfacadeQueryModel(object):

    def __init__(self):
        self._partner_id = None
        self._product_ids = None
        self._request_from = None
        self._status = None
        self._user_id = None

    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def product_ids(self):
        return self._product_ids

    @product_ids.setter
    def product_ids(self, value):
        if isinstance(value, list):
            self._product_ids = list()
            for i in value:
                self._product_ids.append(i)
    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, list):
            self._status = list()
            for i in value:
                self._status.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.product_ids:
            if isinstance(self.product_ids, list):
                for i in range(0, len(self.product_ids)):
                    element = self.product_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_ids[i] = element.to_alipay_dict()
            if hasattr(self.product_ids, 'to_alipay_dict'):
                params['product_ids'] = self.product_ids.to_alipay_dict()
            else:
                params['product_ids'] = self.product_ids
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        if self.status:
            if isinstance(self.status, list):
                for i in range(0, len(self.status)):
                    element = self.status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status[i] = element.to_alipay_dict()
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayPcreditHuabeiPcbenefitcoreBfactivitfacadeQueryModel()
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'product_ids' in d:
            o.product_ids = d['product_ids']
        if 'request_from' in d:
            o.request_from = d['request_from']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


