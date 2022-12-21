#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantSubsidiariesApplyModel(object):

    def __init__(self):
        self._pid = None
        self._service_id = None
        self._smid = None
        self._sub_merchant_contact_number = None
        self._sub_merchant_jump_link = None
        self._sub_merchant_logo_url = None
        self._sub_merchant_name = None
        self._sub_pid = None

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def sub_merchant_contact_number(self):
        return self._sub_merchant_contact_number

    @sub_merchant_contact_number.setter
    def sub_merchant_contact_number(self, value):
        self._sub_merchant_contact_number = value
    @property
    def sub_merchant_jump_link(self):
        return self._sub_merchant_jump_link

    @sub_merchant_jump_link.setter
    def sub_merchant_jump_link(self, value):
        self._sub_merchant_jump_link = value
    @property
    def sub_merchant_logo_url(self):
        return self._sub_merchant_logo_url

    @sub_merchant_logo_url.setter
    def sub_merchant_logo_url(self, value):
        self._sub_merchant_logo_url = value
    @property
    def sub_merchant_name(self):
        return self._sub_merchant_name

    @sub_merchant_name.setter
    def sub_merchant_name(self, value):
        self._sub_merchant_name = value
    @property
    def sub_pid(self):
        return self._sub_pid

    @sub_pid.setter
    def sub_pid(self, value):
        self._sub_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.sub_merchant_contact_number:
            if hasattr(self.sub_merchant_contact_number, 'to_alipay_dict'):
                params['sub_merchant_contact_number'] = self.sub_merchant_contact_number.to_alipay_dict()
            else:
                params['sub_merchant_contact_number'] = self.sub_merchant_contact_number
        if self.sub_merchant_jump_link:
            if hasattr(self.sub_merchant_jump_link, 'to_alipay_dict'):
                params['sub_merchant_jump_link'] = self.sub_merchant_jump_link.to_alipay_dict()
            else:
                params['sub_merchant_jump_link'] = self.sub_merchant_jump_link
        if self.sub_merchant_logo_url:
            if hasattr(self.sub_merchant_logo_url, 'to_alipay_dict'):
                params['sub_merchant_logo_url'] = self.sub_merchant_logo_url.to_alipay_dict()
            else:
                params['sub_merchant_logo_url'] = self.sub_merchant_logo_url
        if self.sub_merchant_name:
            if hasattr(self.sub_merchant_name, 'to_alipay_dict'):
                params['sub_merchant_name'] = self.sub_merchant_name.to_alipay_dict()
            else:
                params['sub_merchant_name'] = self.sub_merchant_name
        if self.sub_pid:
            if hasattr(self.sub_pid, 'to_alipay_dict'):
                params['sub_pid'] = self.sub_pid.to_alipay_dict()
            else:
                params['sub_pid'] = self.sub_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantSubsidiariesApplyModel()
        if 'pid' in d:
            o.pid = d['pid']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'smid' in d:
            o.smid = d['smid']
        if 'sub_merchant_contact_number' in d:
            o.sub_merchant_contact_number = d['sub_merchant_contact_number']
        if 'sub_merchant_jump_link' in d:
            o.sub_merchant_jump_link = d['sub_merchant_jump_link']
        if 'sub_merchant_logo_url' in d:
            o.sub_merchant_logo_url = d['sub_merchant_logo_url']
        if 'sub_merchant_name' in d:
            o.sub_merchant_name = d['sub_merchant_name']
        if 'sub_pid' in d:
            o.sub_pid = d['sub_pid']
        return o


