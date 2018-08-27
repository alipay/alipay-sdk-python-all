#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LicenseInfo(object):

    def __init__(self):
        self._agency = None
        self._gmt_expire = None
        self._gmt_start = None
        self._license_id = None
        self._license_name = None
        self._pic_url = None
        self._result = None
        self._sequence = None
        self._type = None

    @property
    def agency(self):
        return self._agency

    @agency.setter
    def agency(self, value):
        self._agency = value
    @property
    def gmt_expire(self):
        return self._gmt_expire

    @gmt_expire.setter
    def gmt_expire(self, value):
        self._gmt_expire = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def license_id(self):
        return self._license_id

    @license_id.setter
    def license_id(self, value):
        self._license_id = value
    @property
    def license_name(self):
        return self._license_name

    @license_name.setter
    def license_name(self, value):
        self._license_name = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agency:
            if hasattr(self.agency, 'to_alipay_dict'):
                params['agency'] = self.agency.to_alipay_dict()
            else:
                params['agency'] = self.agency
        if self.gmt_expire:
            if hasattr(self.gmt_expire, 'to_alipay_dict'):
                params['gmt_expire'] = self.gmt_expire.to_alipay_dict()
            else:
                params['gmt_expire'] = self.gmt_expire
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.license_id:
            if hasattr(self.license_id, 'to_alipay_dict'):
                params['license_id'] = self.license_id.to_alipay_dict()
            else:
                params['license_id'] = self.license_id
        if self.license_name:
            if hasattr(self.license_name, 'to_alipay_dict'):
                params['license_name'] = self.license_name.to_alipay_dict()
            else:
                params['license_name'] = self.license_name
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.sequence:
            if hasattr(self.sequence, 'to_alipay_dict'):
                params['sequence'] = self.sequence.to_alipay_dict()
            else:
                params['sequence'] = self.sequence
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LicenseInfo()
        if 'agency' in d:
            o.agency = d['agency']
        if 'gmt_expire' in d:
            o.gmt_expire = d['gmt_expire']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'license_id' in d:
            o.license_id = d['license_id']
        if 'license_name' in d:
            o.license_name = d['license_name']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'result' in d:
            o.result = d['result']
        if 'sequence' in d:
            o.sequence = d['sequence']
        if 'type' in d:
            o.type = d['type']
        return o


