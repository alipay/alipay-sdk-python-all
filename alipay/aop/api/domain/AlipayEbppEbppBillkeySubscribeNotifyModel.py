#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppBillkeySubscribeNotifyModel(object):

    def __init__(self):
        self._alipay_join_no = None
        self._billkey = None
        self._city_code = None
        self._inst_join_no = None
        self._join_fail_reason = None
        self._join_result = None
        self._province_code = None

    @property
    def alipay_join_no(self):
        return self._alipay_join_no

    @alipay_join_no.setter
    def alipay_join_no(self, value):
        self._alipay_join_no = value
    @property
    def billkey(self):
        return self._billkey

    @billkey.setter
    def billkey(self, value):
        self._billkey = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def inst_join_no(self):
        return self._inst_join_no

    @inst_join_no.setter
    def inst_join_no(self, value):
        self._inst_join_no = value
    @property
    def join_fail_reason(self):
        return self._join_fail_reason

    @join_fail_reason.setter
    def join_fail_reason(self, value):
        self._join_fail_reason = value
    @property
    def join_result(self):
        return self._join_result

    @join_result.setter
    def join_result(self, value):
        self._join_result = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_join_no:
            if hasattr(self.alipay_join_no, 'to_alipay_dict'):
                params['alipay_join_no'] = self.alipay_join_no.to_alipay_dict()
            else:
                params['alipay_join_no'] = self.alipay_join_no
        if self.billkey:
            if hasattr(self.billkey, 'to_alipay_dict'):
                params['billkey'] = self.billkey.to_alipay_dict()
            else:
                params['billkey'] = self.billkey
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.inst_join_no:
            if hasattr(self.inst_join_no, 'to_alipay_dict'):
                params['inst_join_no'] = self.inst_join_no.to_alipay_dict()
            else:
                params['inst_join_no'] = self.inst_join_no
        if self.join_fail_reason:
            if hasattr(self.join_fail_reason, 'to_alipay_dict'):
                params['join_fail_reason'] = self.join_fail_reason.to_alipay_dict()
            else:
                params['join_fail_reason'] = self.join_fail_reason
        if self.join_result:
            if hasattr(self.join_result, 'to_alipay_dict'):
                params['join_result'] = self.join_result.to_alipay_dict()
            else:
                params['join_result'] = self.join_result
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppBillkeySubscribeNotifyModel()
        if 'alipay_join_no' in d:
            o.alipay_join_no = d['alipay_join_no']
        if 'billkey' in d:
            o.billkey = d['billkey']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'inst_join_no' in d:
            o.inst_join_no = d['inst_join_no']
        if 'join_fail_reason' in d:
            o.join_fail_reason = d['join_fail_reason']
        if 'join_result' in d:
            o.join_result = d['join_result']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


