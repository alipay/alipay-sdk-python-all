#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportVehicleownerCampaignPublishModel(object):

    def __init__(self):
        self._activity_icon = None
        self._activity_record = None
        self._activity_url = None
        self._biz_code = None
        self._effective_end = None
        self._effective_start = None
        self._ext_info = None
        self._last_platform = None
        self._last_store_id = None
        self._out_biz_id = None
        self._priority_booth = None

    @property
    def activity_icon(self):
        return self._activity_icon

    @activity_icon.setter
    def activity_icon(self, value):
        self._activity_icon = value
    @property
    def activity_record(self):
        return self._activity_record

    @activity_record.setter
    def activity_record(self, value):
        self._activity_record = value
    @property
    def activity_url(self):
        return self._activity_url

    @activity_url.setter
    def activity_url(self, value):
        self._activity_url = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def effective_end(self):
        return self._effective_end

    @effective_end.setter
    def effective_end(self, value):
        self._effective_end = value
    @property
    def effective_start(self):
        return self._effective_start

    @effective_start.setter
    def effective_start(self, value):
        self._effective_start = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def last_platform(self):
        return self._last_platform

    @last_platform.setter
    def last_platform(self, value):
        self._last_platform = value
    @property
    def last_store_id(self):
        return self._last_store_id

    @last_store_id.setter
    def last_store_id(self, value):
        self._last_store_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def priority_booth(self):
        return self._priority_booth

    @priority_booth.setter
    def priority_booth(self, value):
        self._priority_booth = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_icon:
            if hasattr(self.activity_icon, 'to_alipay_dict'):
                params['activity_icon'] = self.activity_icon.to_alipay_dict()
            else:
                params['activity_icon'] = self.activity_icon
        if self.activity_record:
            if hasattr(self.activity_record, 'to_alipay_dict'):
                params['activity_record'] = self.activity_record.to_alipay_dict()
            else:
                params['activity_record'] = self.activity_record
        if self.activity_url:
            if hasattr(self.activity_url, 'to_alipay_dict'):
                params['activity_url'] = self.activity_url.to_alipay_dict()
            else:
                params['activity_url'] = self.activity_url
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.effective_end:
            if hasattr(self.effective_end, 'to_alipay_dict'):
                params['effective_end'] = self.effective_end.to_alipay_dict()
            else:
                params['effective_end'] = self.effective_end
        if self.effective_start:
            if hasattr(self.effective_start, 'to_alipay_dict'):
                params['effective_start'] = self.effective_start.to_alipay_dict()
            else:
                params['effective_start'] = self.effective_start
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.last_platform:
            if hasattr(self.last_platform, 'to_alipay_dict'):
                params['last_platform'] = self.last_platform.to_alipay_dict()
            else:
                params['last_platform'] = self.last_platform
        if self.last_store_id:
            if hasattr(self.last_store_id, 'to_alipay_dict'):
                params['last_store_id'] = self.last_store_id.to_alipay_dict()
            else:
                params['last_store_id'] = self.last_store_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.priority_booth:
            if hasattr(self.priority_booth, 'to_alipay_dict'):
                params['priority_booth'] = self.priority_booth.to_alipay_dict()
            else:
                params['priority_booth'] = self.priority_booth
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportVehicleownerCampaignPublishModel()
        if 'activity_icon' in d:
            o.activity_icon = d['activity_icon']
        if 'activity_record' in d:
            o.activity_record = d['activity_record']
        if 'activity_url' in d:
            o.activity_url = d['activity_url']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'effective_end' in d:
            o.effective_end = d['effective_end']
        if 'effective_start' in d:
            o.effective_start = d['effective_start']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'last_platform' in d:
            o.last_platform = d['last_platform']
        if 'last_store_id' in d:
            o.last_store_id = d['last_store_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'priority_booth' in d:
            o.priority_booth = d['priority_booth']
        return o


