#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppAraterRatestatusModifyModel(object):

    def __init__(self):
        self._ext_info = None
        self._havana_id = None
        self._pid = None
        self._rate_biz_source = None
        self._rate_id = None
        self._rate_status = None
        self._route_uid = None
        self._trade_no = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def rate_biz_source(self):
        return self._rate_biz_source

    @rate_biz_source.setter
    def rate_biz_source(self, value):
        self._rate_biz_source = value
    @property
    def rate_id(self):
        return self._rate_id

    @rate_id.setter
    def rate_id(self, value):
        self._rate_id = value
    @property
    def rate_status(self):
        return self._rate_status

    @rate_status.setter
    def rate_status(self, value):
        self._rate_status = value
    @property
    def route_uid(self):
        return self._route_uid

    @route_uid.setter
    def route_uid(self, value):
        self._route_uid = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.havana_id:
            if hasattr(self.havana_id, 'to_alipay_dict'):
                params['havana_id'] = self.havana_id.to_alipay_dict()
            else:
                params['havana_id'] = self.havana_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.rate_biz_source:
            if hasattr(self.rate_biz_source, 'to_alipay_dict'):
                params['rate_biz_source'] = self.rate_biz_source.to_alipay_dict()
            else:
                params['rate_biz_source'] = self.rate_biz_source
        if self.rate_id:
            if hasattr(self.rate_id, 'to_alipay_dict'):
                params['rate_id'] = self.rate_id.to_alipay_dict()
            else:
                params['rate_id'] = self.rate_id
        if self.rate_status:
            if hasattr(self.rate_status, 'to_alipay_dict'):
                params['rate_status'] = self.rate_status.to_alipay_dict()
            else:
                params['rate_status'] = self.rate_status
        if self.route_uid:
            if hasattr(self.route_uid, 'to_alipay_dict'):
                params['route_uid'] = self.route_uid.to_alipay_dict()
            else:
                params['route_uid'] = self.route_uid
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppAraterRatestatusModifyModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'havana_id' in d:
            o.havana_id = d['havana_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'rate_biz_source' in d:
            o.rate_biz_source = d['rate_biz_source']
        if 'rate_id' in d:
            o.rate_id = d['rate_id']
        if 'rate_status' in d:
            o.rate_status = d['rate_status']
        if 'route_uid' in d:
            o.route_uid = d['route_uid']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


