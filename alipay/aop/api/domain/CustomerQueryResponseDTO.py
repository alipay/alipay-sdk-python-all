#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomerQueryResponseDTO(object):

    def __init__(self):
        self._bid = None
        self._ep_cert_no = None
        self._ep_name = None
        self._owner_bd_name = None
        self._owner_bd_work_no = None

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def owner_bd_name(self):
        return self._owner_bd_name

    @owner_bd_name.setter
    def owner_bd_name(self, value):
        self._owner_bd_name = value
    @property
    def owner_bd_work_no(self):
        return self._owner_bd_work_no

    @owner_bd_work_no.setter
    def owner_bd_work_no(self, value):
        self._owner_bd_work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid:
            if hasattr(self.bid, 'to_alipay_dict'):
                params['bid'] = self.bid.to_alipay_dict()
            else:
                params['bid'] = self.bid
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.owner_bd_name:
            if hasattr(self.owner_bd_name, 'to_alipay_dict'):
                params['owner_bd_name'] = self.owner_bd_name.to_alipay_dict()
            else:
                params['owner_bd_name'] = self.owner_bd_name
        if self.owner_bd_work_no:
            if hasattr(self.owner_bd_work_no, 'to_alipay_dict'):
                params['owner_bd_work_no'] = self.owner_bd_work_no.to_alipay_dict()
            else:
                params['owner_bd_work_no'] = self.owner_bd_work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerQueryResponseDTO()
        if 'bid' in d:
            o.bid = d['bid']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'owner_bd_name' in d:
            o.owner_bd_name = d['owner_bd_name']
        if 'owner_bd_work_no' in d:
            o.owner_bd_work_no = d['owner_bd_work_no']
        return o


