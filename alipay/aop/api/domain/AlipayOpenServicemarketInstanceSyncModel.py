#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenServicemarketInstanceSyncModel(object):

    def __init__(self):
        self._consumer_uid = None
        self._effect_date = None
        self._event = None
        self._expire_date = None
        self._fin_tech_product_code = None
        self._gmt_modified = None
        self._instance_id = None
        self._instance_status = None
        self._out_biz_no = None

    @property
    def consumer_uid(self):
        return self._consumer_uid

    @consumer_uid.setter
    def consumer_uid(self, value):
        self._consumer_uid = value
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def fin_tech_product_code(self):
        return self._fin_tech_product_code

    @fin_tech_product_code.setter
    def fin_tech_product_code(self, value):
        self._fin_tech_product_code = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def instance_status(self):
        return self._instance_status

    @instance_status.setter
    def instance_status(self, value):
        self._instance_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.consumer_uid:
            if hasattr(self.consumer_uid, 'to_alipay_dict'):
                params['consumer_uid'] = self.consumer_uid.to_alipay_dict()
            else:
                params['consumer_uid'] = self.consumer_uid
        if self.effect_date:
            if hasattr(self.effect_date, 'to_alipay_dict'):
                params['effect_date'] = self.effect_date.to_alipay_dict()
            else:
                params['effect_date'] = self.effect_date
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.fin_tech_product_code:
            if hasattr(self.fin_tech_product_code, 'to_alipay_dict'):
                params['fin_tech_product_code'] = self.fin_tech_product_code.to_alipay_dict()
            else:
                params['fin_tech_product_code'] = self.fin_tech_product_code
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.instance_status:
            if hasattr(self.instance_status, 'to_alipay_dict'):
                params['instance_status'] = self.instance_status.to_alipay_dict()
            else:
                params['instance_status'] = self.instance_status
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketInstanceSyncModel()
        if 'consumer_uid' in d:
            o.consumer_uid = d['consumer_uid']
        if 'effect_date' in d:
            o.effect_date = d['effect_date']
        if 'event' in d:
            o.event = d['event']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'fin_tech_product_code' in d:
            o.fin_tech_product_code = d['fin_tech_product_code']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'instance_status' in d:
            o.instance_status = d['instance_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


