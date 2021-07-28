#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherTemplateInfo import VoucherTemplateInfo


class MarketActivityInfo(object):

    def __init__(self):
        self._activity_id = None
        self._activity_name = None
        self._brand_logo = None
        self._brand_name = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._status = None
        self._voucher_infos = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voucher_infos(self):
        return self._voucher_infos

    @voucher_infos.setter
    def voucher_infos(self, value):
        if isinstance(value, list):
            self._voucher_infos = list()
            for i in value:
                if isinstance(i, VoucherTemplateInfo):
                    self._voucher_infos.append(i)
                else:
                    self._voucher_infos.append(VoucherTemplateInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.publish_start_time:
            if hasattr(self.publish_start_time, 'to_alipay_dict'):
                params['publish_start_time'] = self.publish_start_time.to_alipay_dict()
            else:
                params['publish_start_time'] = self.publish_start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.voucher_infos:
            if isinstance(self.voucher_infos, list):
                for i in range(0, len(self.voucher_infos)):
                    element = self.voucher_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_infos[i] = element.to_alipay_dict()
            if hasattr(self.voucher_infos, 'to_alipay_dict'):
                params['voucher_infos'] = self.voucher_infos.to_alipay_dict()
            else:
                params['voucher_infos'] = self.voucher_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketActivityInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'status' in d:
            o.status = d['status']
        if 'voucher_infos' in d:
            o.voucher_infos = d['voucher_infos']
        return o


